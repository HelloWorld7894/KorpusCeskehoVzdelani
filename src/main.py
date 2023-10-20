from flask import Flask, render_template
from flask_socketio import SocketIO

import process_data
import document_parser
import webscraper

#init
app = Flask(__name__, template_folder='templates', static_folder='static')
socketio = SocketIO(app)

#set classification for chatGPT
process_data.set_classification()

@app.route("/")
def main():
    return render_template("index.html")

@socketio.on("conn_valid")
def handle_connection(data):
    print("Got a connection! " + data)

    web_input = "Církevní gymnázium Plzeň"

    webscraper.search_for_schools(web_input)
    output = document_parser.parse_docs()

    #feed to ChatGPT
    for out_obj in output:
        out = process_data.prompt(out_obj["text"])
        print(out)

    #load data
    socketio.emit("data", "data_test")

if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True)