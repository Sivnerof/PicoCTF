# PW Crack 2

## Description

Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/14/level2.py "Pico CTF link to download Python password checker program") and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/14/level2.flag.txt.enc "Pico CTF link to download encrypted flag text file") in the same directory too.

## Hints

* Does that encoding look familiar?

* The str_xor function does not need to be reverse engineered for this challenge.

## Walkthrough

```python
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level2.flag.txt.enc', 'rb').read()



def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_2_pw_check()

```

```python
def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```

```python
if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
```

```
chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)
```

```
$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> chr(0x34)
'4'
>>> chr(0x65)
'e'
>>> chr(0x63)
'c'
>>> chr(0x39)
'9'
```

```
$ python3 level2.py
Please enter correct password for flag: 4ec9
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_9701e681}
```

```picoCTF{tr45h_51ng1ng_9701e681}```
