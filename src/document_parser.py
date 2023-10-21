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
                idx = full_txt.find("Závěry")
                top_parse = full_txt[idx:]

                idx = top_parse.find("Seznam dokladů")
                bot_parse = top_parse[:idx]

            elif pdf_idx == "2":

                #parse txt to get rid of useless parts
                idx = full_txt.find("Celkové hodnocení školy")
                top_parse = full_txt[idx:]

                idx = top_parse.find("Seznam písemností,")
                bot_parse = top_parse[:idx]

            elif pdf_idx == "3":

                #parse txt to get rid of useless parts
                idx = full_txt.find("ZÁVĚR")
                top_parse = full_txt[idx:]

                idx = top_parse.find("Razítko")
                bot_parse = top_parse[:idx]
            
            elif pdf_idx == "4":

                #parse txt to get rid of useless parts
                idx = full_txt.find("ZÁVĚR")
                top_parse = full_txt[idx:]

                idx = top_parse.find("Razítko")
                bot_parse = top_parse[:idx]

            text_obj["label"] = file_path.replace("./src/cache/", "").replace(".pdf", "")[:-2]
            text_obj["text"] = bot_parse
            
            all_text.append(text_obj)

    return all_text

if __name__ == "__main__":
    print(os.getcwd())
    parse_docs()