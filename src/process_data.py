import numpy as np
import csv
import openai
import yaml

#setup
API_KEY = ""

with open("config.yaml", "r") as stream:
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

def set_binary_cls():
    prompt()

def main():
    pass

if __name__ == "__main__":
    #just for testimng
    chat_in = "Explain quantum mechanics please"
    response = prompt(chat_in)

    print(response)