import requests
from bs4 import BeautifulSoup
import yaml
import os

#init
MAX_REPORT_SIZE = 0

with open("config.yaml", "r") as stream:
    try:
        MAX_REPORT_SIZE = yaml.safe_load(stream)["MAX_REPORT_SIZE"]
    except yaml.YAMLError as exc:
        print(exc)

base_url = "https://csicr.cz/cz/Registr-inspekcnich-zprav?page=undefined&jmeno=&adresa=&mesto=&ic=&identifikator="

def search_for_schools(school_string):
    #fetch main page
    url = base_url.replace("jmeno=", "jmeno=" + school_string)

    request = requests.get(url)
    soup = BeautifulSoup(request.content, "html.parser")
    tbody = soup.select_one("tbody")
    school = tbody.select_one("td")
    school_link = school.select_one("a")
    
    school_link = school_link.get("href")

    data_url = url[:url.find("page=")]
    data_url += school_link

    print(data_url)

    #fetch tables
    request = requests.get(data_url)
    soup = BeautifulSoup(request.content, "html.parser")

    #delete all pdfs
    for i, filename in enumerate(os.listdir("./src/cache/")):
        file_path = os.path.join("./src/cache/", filename)
        # checking if it is a file
        if os.path.isfile(file_path):
            os.remove(file_path)

    #fetch all reports
    tbody = soup.select_one("tbody")
    for i in range(int(MAX_REPORT_SIZE)):
        tr = tbody.select("tr")[i]

        td_text = tr.select("td")[1]
        td_spec = tr.select("td")[2]
        link = td_spec.select_one("a").get("href")
        
        response = requests.get(link)

        label = str(td_text.contents[0]).strip()
        label = label[6:]

        pdf = open("./src/cache/"+label+"n"+str(i)+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()

if __name__ == "__main__":
    search_for_schools("Církevní gymnázium Plzeň")