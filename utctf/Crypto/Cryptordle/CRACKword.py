#!/usr/bin/env python3

from Crypto.Util.number import *

from pwn import *

io = remote('betta.utctf.live', 7496)
guess = ['bbbbb', 'bbbba', 'bbbab', 'bbabb', 'babbb']

def get_out(g):
    print(io.recvline())
    io.sendline(g)
    return int(io.recvline().decode())
    
for i in range(3):
    r51 = get_out(guess[0])
    r52 = get_out(guess[1])
    r53 = get_out(guess[2])
    r54 = get_out(guess[3])
    r55 = get_out(guess[4])
    for b5 in range(26):
       for b4 in range(26):
          for b3 in range(26):
              for b2 in range(26):
                  for b1 in range(26):
                      if ( (1-b1) * (1-b2) * (1-b3) * (1-b4) * (1-b5)) % 31 == r51 and \
                       ( (1-b1) * (1-b2) * (1-b3) * (1-b4) * (0-b5)) % 31 == r52 and \
                       ((1-b1) * (1-b2) * (1-b3) * (0-b4) * (1-b5)) % 31 == r53 and \
                       ((1-b1) * (1-b2) * (0-b3) * (1-b4) * (1-b5)) % 31 == r54 and \
                       ((1-b1) * (0-b2) * (1-b3) * (1-b4) * (1-b5)) % 31 == r55:
                           flag=f'{chr(b1+97)+chr(b2+97)+chr(b3+97)+chr(b4+97)+chr(b5+97)}'
                           break
    io.sendline(flag.encode())
    print(flag)
    print(io.recvline())
    print(io.recvline())

io.interactive()
#flag=utflag{sometimes_pure_guessing_is_the_strat}'''
