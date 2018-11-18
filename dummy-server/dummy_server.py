from flask import Flask
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():

    now = str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    html = "<meta http-equiv=\"refresh\" content=\"1\">" \
           "<h2>Hello {name}!</h2>" \
           "<b>Current date & time</b> {dt}<br/>" 
    return html.format(name=os.getenv("NAME", "world"),dt=now)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
