#coding: utf-8

import rsa
import gmpy

n = 76775333340223961139427050707840417811156978085146970312315886671546666259161

p = 273821108020968288372911424519201044333

q = 280385007186315115828483000867559983517

65537

d = int(gmpy.invert(e,(p-1)*(q-1)))

pk = rsa.PrivateKey(n,e,d,p,q)

with open("fllllllag.txt","rb") as f:
	print rsa.decrypt(f.read(),pk),decode()