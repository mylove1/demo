#!/usr/bin/env python
# coding:utf-8
from contextlib import closing
import requests


if __name__ == "__main__":

    # url = "http://pic.meizitu.com/wp-content/uploads/2016a/08/10/01.jpg"
    # with closing(requests.get(url, stream=True)) as r:
    #     print r.status_code
    #     print r.headers
    #
    #     with open(r"E:\bizhi\mezi.jpg", "wb") as f:
    #         f.write(r.content)
    #     print "ok"

    url = "http://pic.meizitu.com/wp-content/uploads/2016a/08/10/01.jpg"
    r = requests.get(url, stream=True)
    print r.status_code
    print r.headers
    with open(r"E:\bizhi\mezi.jpg", "wb") as f:
        f.write(r.content)
    print "ok"

