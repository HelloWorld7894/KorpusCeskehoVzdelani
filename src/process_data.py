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
    with open("../data/") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())

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