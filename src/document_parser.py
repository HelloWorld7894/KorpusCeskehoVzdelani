import PyPDF2
import os

def parse_docs():
    path = "./src/cache/"

    all_text = []

    for i, filename in enumerate(os.listdir(path)):
        file_path = os.path.join(path, filename)
        # checking if it is a file
        if os.path.isfile(file_path):

            text_obj = {}

            reader = PyPDF2.PdfReader(file_path)

            full_txt = ""
            for page in reader.pages:
                full_txt += page.extract_text()


            #For some reason ČSI labels all pdfs differently every year
            pdf_idx = file_path.replace("./src/cache/", "").replace(".pdf", "")[-1]
            if pdf_idx == "0" or pdf_idx == "1":

                #parse txt to get rid of useless parts
                idx = full_txt.find("Charakteristika")
                top_parse = full_txt[idx:]

                idx = top_parse.find("Poučení")
                bot_parse = top_parse[:idx]

            elif pdf_idx == "2":

                #parse txt to get rid of useless parts
                idx = full_txt.find("školy")
                top_parse = full_txt[idx:]

                idx = top_parse.find("Seznam písemností,")
                bot_parse = top_parse[:idx]

            elif pdf_idx == "3":

                #parse txt to get rid of useless parts
                idx = full_txt.find("Zjišťování a hodnocení formálních")
                top_parse = full_txt[idx:]

                idx = top_parse.find("Složení inspekčního týmu a datum vyhotovení inspekční zprávy")
                bot_parse = top_parse[:idx]
            
            elif pdf_idx == "4":

                #parse txt to get rid of useless parts
                idx = full_txt.find("Signatura")
                top_parse = full_txt[idx:]

                idx = top_parse.find("Složení inspekčního týmu a datum vyhotovení inspekční zprávy")
                bot_parse = top_parse[:idx]

            text_obj["label"] = file_path.replace("./src/cache/", "").replace(".pdf", "")[:-2]
            text_obj["text"] = bot_parse
            
            #charlen = len(text_obj["text"])
            #if charlen > 13000: #this is hardcoded
            #    text_obj["text"] = bot_parse[int(3 * (charlen / 4)):]


            all_text.append(text_obj)

    return all_text

if __name__ == "__main__":
    print(os.getcwd())
    parse_docs()