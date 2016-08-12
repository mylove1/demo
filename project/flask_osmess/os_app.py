# -*- coding:utf-8 -*-
from flask import Flask, render_template, request
import psutil
import psutil
import json
import time
net = psutil.net_io_counters()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def net_info():
    data = []
    net_recv = '{0:.2f} kb'.format(net.bytes_recv / 1024)
    net_send = '{0:.2f} kb'.format(net.bytes_sent / 1024)
    data.append([net_recv,time.time()])
    return json.dumps(data)


def main():
    app.run(host='0.0.0.0', port=9901)


if __name__ == '__main__':
    main()

