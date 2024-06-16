# PW Crack 2

## Description

Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/14/level2.py "Pico CTF link to download Python password checker program") and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/14/level2.flag.txt.enc "Pico CTF link to download encrypted flag text file") in the same directory too.

## Hints

* Does that encoding look familiar?

* The str_xor function does not need to be reverse engineered for this challenge.

## Walkthrough

We're told in the CTF description that the program provided to us is a password checker. If we do a quick scan of the code, we can verify this.

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

While scanning through the code, the function named ```level_2_pw_check``` stands out.

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

It seems that the program takes an encrypted flag found in the text file named [level2.flag.txt.enc](./level2.flag.txt.enc "Encrypted flag text file") and will print it out after decrypting it, but only if the password provided is equal to ```chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)```.

```python
if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
    print("Welcome back... your flag, user:")
    decryption = str_xor(flag_enc.decode(), user_pw)
    print(decryption)
    return
```

A simple attempt at obfuscation is used here to make the password more difficult to find. Instead of hardcoding the password directly as a string, each character of the password is represented by its hexadecimal value and converted to a character using the ```chr()``` function. These characters are then concatenated to form the password string, which is then checked against the user input.

We can check the character representations of these hexadecimal values to retrieve the actual password using the Python interpreter.

```
$ python3

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
$ python3

>>> chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)
'4ec9'
```

After using the Python interpreter, we'll find that the password is ```4ec9```. We can verify this by running the Python password checker program provided to us and using the newly found password as input when prompted. Doing so will reveal the CTF flag.

```
$ python3 level2.py
Please enter correct password for flag: 4ec9
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_9701e681}
```

```picoCTF{tr45h_51ng1ng_9701e681}```
