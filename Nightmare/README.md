## Nightmare
https://guyinatuxedo.github.io/index.html

Nightmare is an intro to binary exploitation / reverse engineering course based around ctf challenges. I call it that because 
it's a lot of people's nightmare to get hit by weaponized 0 days, which these skills directly translate into doing that type 
of work (plus it's a really cool song).




### Assembly RE
`~ cd AssemblyRE`
Reversing For each challenge, try to write write the C code.

#### Hello, World
Open the assembly file in Ghidra.  
Go to `_start` function to see that it calls main
puts assembly is printing a string `hello, world` to the terminal
`gcc hello.c -o helloworld
./helloworld`

#### IfThen
For this one I opened the file in GDB.
`
~ gdb ./if_then
(gdb) break main
(gdb) run
(gdb) disassemble
`
You will notice here that there is a `mov DWORD PTR [ebp-0xc],0xa`
immediately followed by a `cmp DWORD PTR [ebp-0xc],0xa` 
This will see if the register ebp - 0xc has the value 0xa.  Which of course it does because it was just set.  If true jump to past the <main+0x2e> and proceeds to the following instructions
`
sub esp,0xc
push 0x80484c0
call 0x80482d0
`
and what is stored at 0x80482d0? 
the <puts@plt> of course.  which prints the string x = ten

#### Loop
`objdump -D loop -M intel | less`
scroll down until you get to main.
Probably recommended to read the assembly first to get an idea of what is happening in the code.  Don't accidentally run malware on your host machine. 