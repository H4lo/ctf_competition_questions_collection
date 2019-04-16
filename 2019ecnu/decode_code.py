s = "bg[`sZ*Zg'dPfP`VM_SXVd"
flag = ''
add = 4
for i in range(len(s)):
	
	flag += chr(ord(s[i])+add)
	add +=1
		
		
print flag