from flask import Flask
import os
import socket
from datetime import datetime

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    now = str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    html = "<head><meta charset=\"UTF-8\"><meta http-equiv=\"refresh\" content=\"1\"></head>" \
           "<h2>Hello {name}!</h2>" \
           "<b>Current date & time</b> {dt}<br/>" 
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"),dt=now,visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
