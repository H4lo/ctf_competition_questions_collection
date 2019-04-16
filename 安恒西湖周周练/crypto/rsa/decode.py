#coding: utf-8

import rsa
import gmpy

n = 86934482296048119190666062003494800588905656017203025617216654058378322103517

p = 285960468890451637935629440372639283459

q = 304008741604601924494328155975272418463

65537

d = int(gmpy.invert(e,(p-1)*(q-1)))

pk = rsa.PrivateKey(n,e,d,p,q)

with open("flag.enc","rb") as f:
	print rsa.decrypt(f.read(),pk),decode()