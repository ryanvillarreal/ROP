#!/usr/bin/python
from pwn import *

# setup pwntools
elf = context.binary = ELF('badchars32')

# get base address
info("%#x <-- base address" % elf.address)

