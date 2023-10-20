import numpy as np
import csv
import openai
import yaml

#test imports
import document_parser

#setup
API_KEY = ""
START_PROMPT = """
Mohl by jsi fungovat jako model co bude hodnotit školu ve škále od 0 do 10 podle textu co ti zde zadám? Zpráva vždy bude začínat slovem analyzuj. Přičemž odpověď musí za každých okolností vždy být pouze to číslo
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

def main():
    pass

if __name__ == "__main__":
    #just for testing
    set_classification()
    chat_in = document_parser.parse_doc()
    response = prompt(chat_in)

    print(response)