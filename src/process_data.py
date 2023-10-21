import numpy as np
import openai
import yaml
from bs4 import BeautifulSoup
import os
import json
import xmltodict

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
MAX_COLS = 7

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
    with open("./data/selected/GymnaziaAll.xml") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())



        json_data = data_dict["vdbData"]["data"]["udaj"]

        slices = []

        for i, value in enumerate(json_data):
            slice = {
                "schools": 0,
                "classes": 0,
                "students-all": 0,
                "students-women": 0,
                "students-men": 0,
                "1rocnik": 0,
                "absolventi": 0
            }
            
            try:
                if i % 7 == 0:
                    slice["schools"] = value["hod"]
                elif i % 7 == 1:
                    slice["classes"] = value["hod"]
                elif i % 7 == 2:
                    slice["students-all"] = value["hod"]
                elif i % 7 == 3:
                    slice["students-women"] = value["hod"]
                elif i % 7 == 4:
                    slice["students-men"] = value["hod"]
                elif i % 7 == 5:
                    slice["1rocnik"] = value["hod"]
                elif i % 7 == 6:
                    slice["absolventi"] = value["hod"]
            except(KeyError):
                if i % 7 == 0:
                    slice["schools"] = 0
                elif i % 7 == 1:
                    slice["classes"] = 0
                elif i % 7 == 2:
                    slice["students-all"] = 0
                elif i % 7 == 3:
                    slice["students-women"] = 0
                elif i % 7 == 4:
                    slice["students-men"] = 0
                elif i % 7 == 5:
                    slice["1rocnik"] = 0
                elif i % 7 == 6:
                    slice["absolventi"] = 0

            slices.append(slice)
        print(slices)

def load_predefined_chatgpt_data():
    #load GLP
    file_GLP = open("./chatgpt_cache/GLP.json")
    json_GLP = json.load(file_GLP)
    string_GLP = json.dumps(json_GLP, ensure_ascii=False)

    file_MG = open("./chatgpt_cache/GLP.json")
    json_MG = json.load(file_MG)
    string_MG = json.dumps(json_MG, ensure_ascii=False)

    return [string_GLP, string_MG]

if __name__ == "__main__":
    #load_predefined_chatgpt_data()
    load_all_data()