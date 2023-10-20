from flask import Flask, render_template
from flask_socketio import SocketIO

import process_data

app = Flask(__name__, template_folder='templates', static_folder='static')
socketio = SocketIO(app)

@app.route("/")
def main():
    return render_template("index.html")

@socketio.on("conn_valid")
def handle_connection(data):
    print("Got a connection! " + data)

    #put all the loading data here
    #TODO
    process_data.main()

    #load data
    socketio.emit("data", "data_test")

if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True)