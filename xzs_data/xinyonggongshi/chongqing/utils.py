#!/usr/bin/env python
# coding:utf-8

import requests

def get_html(url, coding=False, proxy=False, check_func=False,):
	check_num = 0
	while 1:
		check_num += 1
		if proxy:
			pass

		r = requests.get(url,proxies=proxy)
		if coding:
			r.encoding = coding
		if check_func:
			pass
		return r.text
