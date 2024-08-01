# Patchme.py

## Description

Can you get the flag? Run this [Python program](https://artifacts.picoctf.net/c/200/patchme.flag.py "Pico CTF link to download Python program") in the same directory as this [encrypted flag](https://artifacts.picoctf.net/c/200/flag.txt.enc "Pico CTF link to download encoded flag").

## Hints

* (None)

## Walkthrough

If we look through the source code for the Python program provided in the room description, [patchme.flag.py](./patchme.flag.py "Python program needed to solve patchme.py challenge"), we'll see the following code:

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


flag_enc = open('flag.txt.enc', 'rb').read()


def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")


level_1_pw_check()
```

The Python program reads an encoded text file, named [flag.txt.enc](./flag.txt.enc "Encoded flag text file"), which contains a flag and checks if the user input provided is equal to the hardcoded password. If so, it decodes the flag and prints it out.

The password can be found within the conditional statement, as a multi-line string, in the ```level_1_pw_check``` function.

```python
if( user_pw == "ak98" + \
                "-=90" + \
                "adfjhgj321" + \
                "sleuth9000"):
```

Putting the string together we get "ak98-=90adfjhgj321sleuth9000".

Now that we have the pasword we can run the program and print the flag.

```
$ python3 patchme.flag.py
Please enter correct password for flag: ak98-=90adfjhgj321sleuth9000
Welcome back... your flag, user:
picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}
```

```picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}```
