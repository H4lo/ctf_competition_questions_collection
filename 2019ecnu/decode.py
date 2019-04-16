# coding: utf-8
import requests
import re

#res = requests.session()

def exp():
	url = "http://47.103.43.235:82/web/a/index.php"
	html = requests.get(url)
	print html.text
	
if __name__ == '__main__':
	exp()