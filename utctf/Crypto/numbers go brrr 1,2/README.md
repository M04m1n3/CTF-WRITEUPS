# Crypto

## numbers go brrr


### Info

![](screenshots/1.png)

 first challenge was basically just generate a random seed (can be brutforced) then genereate am AES key using this seed with a  function  so the solution is to bruteforce the seed to get the exact seed that generate the exact AES key since the seed doesnt change in the session so:
 
```python

#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

def get_random_number():
    global seed 
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed

def decrypt(c):
    key = b''
    for i in range(8):
        key += (get_random_number() % (2 ** 16)).to_bytes(2, 'big')
    cipher = AES.new(key, AES.MODE_ECB)
    plain = cipher.decrypt(pad(c, AES.block_size))
    plain = unpad(plain,AES.block_size)
    return plain
    
c=[here the flag encrypted from the server]
ciphertext = bytes.fromhex(c)
for i in range(1000000):
    seed = i
    flag=decrypt(ciphertext)
    if b'utflag{'in flag:
    	print(flag)
    	break
#utflag{deep_seated_and_recurring_self-doubts}
```
  
## numbers go brrr2


### Info

![](screenshots/2.png)

it was a revenge maybe? but same solution just u have to use exact way that the server is using the sequences because now the seed and the key changes everytime and you have to guess it three times to get the flag

repeat this one three times and every time pass the guessed key to the server and u will get the flag:

```python
def get_random_number():
    global seed 
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed
    
def encrypt(message):
    key = b''
    for i in range(8):
        key += (get_random_number() % (2 ** 16)).to_bytes(2, 'big')
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return key.hex(), ciphertext.hex()
c='d8b71c40844c5fe15dec19beb722710b'[here the encrypted message ]

for i in range(1000000):
    seed = i
    plain='amine' 
    key = encrypt(b"random text to initalize key")[0]
    key, ciphertext = encrypt(plain.encode())
    if(ciphertext==c):
    	
        	print("Here is your guessed key:",key)
                
        	break
```bash
┌──(mo㉿ElMo)-[~]
└─$  nc guppy.utctf.live 2435 
Thanks for using our encryption service! To get the start guessing, type 1. To encrypt a message, type 2.
You will need to guess the key (you get 250 guesses for one key). You will do this 3 times!
Find the key 1 of 3!
What would you like to do (1 - guess the key, 2 - encrypt a message)?
2
What is your message?
amine
Here is your encrypted message: 17656f38f79524df2c26220af11c59c1
What would you like to do (1 - guess the key, 2 - encrypt a message)?
1
You have 250 guesses to find the key!
What is your guess (in hex)?
dfc61f9fcf0bdf9ba24f9ff32f9aa117
You found the key!
Find the key 2 of 3!
What would you like to do (1 - guess the key, 2 - encrypt a message)?
2
What is your message?
amine
Here is your encrypted message: 2514e0250765cb0d15185727b374d3b0
What would you like to do (1 - guess the key, 2 - encrypt a message)?
1
You have 250 guesses to find the key!
What is your guess (in hex)?
6aa2a89a7097c6cbde7f9d8bd58f328c
You found the key!
Find the key 3 of 3!
What would you like to do (1 - guess the key, 2 - encrypt a message)?
2
What is your message?
amine
Here is your encrypted message: a2b6b74de98ceec4c36e251049338f7d
What would you like to do (1 - guess the key, 2 - encrypt a message)?
1
You have 250 guesses to find the key!
What is your guess (in hex)?
e47cae35a57fda060a3fda1129a70492
You found the key!
Here is the flag: utflag{ok_you_are_either_really_lucky_or_you_solved_it_as_intended_yay}
```


