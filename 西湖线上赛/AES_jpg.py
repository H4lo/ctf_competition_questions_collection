#-*- coding:utf-8 -*-

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import os
import pdb

#仅适用于jpg格式图片

class Pcrypt():
    def __init__(self, key, file):
        #密钥
        self.key = key
        #要加密的文件绝对路径
        self.file = file
        #要加/解密的图片数据
        self.data = ""
        #保留文件头
        self.header = ""
        self.plain = ""
        self.cipher = ""
        self.cryptor = AES.new(self.key, AES.MODE_CBC, self.key)

    #读取要加密的数据块
    def getData(self):
        f = open(self.file, 'rb')
        self.data = b2a_hex(f.read())
        p = self.data.find(b'ff00') + 4
        print(p)
        #取图片头
        self.header = self.data[:p]
        #取图片数据部分
        self.data = self.data[p:self.data.rfind(b'ffd9')]
        f.close()

    #加密并保存
    def savEdata(self):
        nfile = os.path.abspath(self.file)[:self.file.find('.')] + 'E.jpg'
        self.getData()
        f = open(nfile, 'wb')
        #加上文件头、尾后保存
        f.write(a2b_hex(self.header) + self.encrypt() + b"\xff\xd9")
        f.close()

    #解密并保存
    def savDdata(self):
        nfile = os.path.abspath(self.file)[:self.file.find('.')] + 'D.jpg'
        self.getData()
        f = open(nfile, 'wb')
        f.write(a2b_hex(self.header) + self.decrypt() + b"\xff\xd9")
        f.close()

    #加密
    def encrypt(self):
        length = 16
        count = len(self.data)
        if(count % length != 0):
            add = length - (count % length)
        else:
            add = 0
        data = self.data + (b'\0' * add)

        self.cipher = self.cryptor.encrypt(data)
        return self.cipher
     
    #解密
    def decrypt(self):
        self.plain = self.cryptor.decrypt(a2b_hex(self.data))
        return a2b_hex(self.plain.rstrip('\0'.encode('utf-8')))

def main():
    key = "keyskeyskeyskeys"
    file = input("Pls input target file's abspath(Only support jpg): ")
    p = Pcrypt(key ,file)
    mode = input("decrypt or encrypt(d/e):")
    if(mode == 'd'):
        p.savDdata()
    elif(mode == 'e'):
        p.savEdata()
    else:
        print("Wrong mode!")

if __name__ == '__main__':
    main()
