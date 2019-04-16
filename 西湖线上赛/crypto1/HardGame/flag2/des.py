import base64
from pyDes import *
from random import choice
import string

def GenPassword(length=8,chars=string.ascii_letters):
    return ''.join([choice(chars) for i in range(length)])
 

def DesEncrypt(str):
    k = des(Des_Key, ECB, pad=None, padmode=PAD_PKCS5)
    EncryptStr = k.encrypt(str)
    return EncryptStr.encode('hex')

Des_Key = GenPassword().upper()

f1 = open('123.txt','rb')
f2 = open('enc.txt','wb')
content = f1.read()
res = content.split(',')
for i in range(len(res)):
	if len(res[i])>10:
		f2.write(DesEncrypt(res[i])+'\n')
f1.close()
f2.close()


