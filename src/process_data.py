import numpy as np
import openai
import yaml
from bs4 import BeautifulSoup
import os

#test imports
import document_parser

#setup
API_KEY = ""
DATA_PATH = "./data/"
START_PROMPT_old = """
Mohl by jsi fungovat jako model co bude hodnotit školu ve škále od 0 do 10 podle textu co ti zde zadám? Zpráva vždy bude začínat slovem analyzuj. Přičemž odpověď musí za každých okolností vždy být pouze to číslo
"""

START_PROMPT = """
    pojďme si zahrát hru, vždycky, když ti já napíšu zprávu "analyzuj:" + nějaká zpráva podle které musíš ohodnotit jak se řídí škola a následně ohodnocení vypsat do škály od 0 do 10. Přičemž tady musíš vypsat jen číslo, žádný text
"""

with open("secret_config.yaml", "r") as stream:
    try:
        API_KEY = yaml.safe_load(stream)["api-key"]
    except yaml.YAMLError as exc:
        print(exc)

openai.api_key = API_KEY


#functions
def prompt(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def set_classification():
    #a prompt to set up chatGPT to classification from 0 to 10
    prompt(START_PROMPT)

def load_all_data():
    for i, filename in enumerate(os.listdir(DATA_PATH)):
        file_path = os.path.join(DATA_PATH, filename)
        # checking if it is a file
        if os.path.isfile(file_path) and ".gitignore" not in file_path:
            
            out_array = []
            # Creating own dataset
            # | label: 
            # | array: 
        
            with open(file_path, 'r') as f:
                file_data = f.read()

                Bs_data = BeautifulSoup(file_data, "xml")

                data_div = Bs_data.find("data")
                data = data_div.find_all("udaj")
                print(len(data))

                out = []
                for iy in range(int(len(data) / 4)): #4 columns
                    row = []

                    for ix in range(4):
                        value = data[iy * ix].find("hod").text

                        row.append(value)

                    out.append(row)

                print(out)

if __name__ == "__main__":
    """
    #just for testing
    set_classification()
    chat_in = document_parser.parse_doc()
    response = prompt(chat_in)

    print(response)
    """
    load_all_data()