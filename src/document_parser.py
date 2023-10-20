import PyPDF2
import os

def parse_doc(doc_loc):
    reader = PyPDF2.PdfReader(doc_loc)

    full_txt = ""
    for page in reader.pages:
        full_txt += page.extract_text()

    #parse txt to get rid of useless parts
    idx = full_txt.find("Charakteristika")
    top_parse = full_txt[idx:]

    idx = top_parse.find("Poučení")
    bot_parse = top_parse[:idx]

    return bot_parse

if __name__ == "__main__":
    print(os.getcwd())
    parse_doc("./src/cache/CirkevniGymnazium.pdf")
