from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(0.5)

def goto_url():
    driver.get("https://csicr.cz/cz/Registr-inspekcnich-zprav")

def get_school_data(school_string):
    driver.find_element()

if __name__ == "__main__":
    pass