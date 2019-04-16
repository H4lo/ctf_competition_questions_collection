import hashlib
 
flag2 = "123321@DBApp"
 
for i in range(100000,999999):
        h2 = hashlib.sha1(str(i)+flag2)
        flags = h2.hexdigest()
        if "27019e688a4" in flags:
                print (str(i)+flag2)
                print flags