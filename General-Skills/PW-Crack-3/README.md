# PW Crack 3

## Description

Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/18/level3.py "PicoCTF link to download PW Crack level 3 password checker program") and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/18/level3.flag.txt.enc "PicoCTF link to download PW Crack level 3 encrypted flag text file") and the [hash](https://artifacts.picoctf.net/c/18/level3.hash.bin "PicoCTF link to download PW Crack level 3 hash binary file") in the same directory too. There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## Hints

* To view the level3.hash.bin file in the webshell, do: $ bvi level3.hash.bin

* To exit bvi type :q and press enter.

* The str_xor function does not need to be reverse engineered for this challenge.

## Walkthrough

If we open the [level 3 python password checker program](./level3.py "Level 3 python password checker program") we'll see the following code.

```python
import hashlib

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

flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_3_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_3_pw_check()


# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]

```

The Python program takes a [binary file that contains a hashed password](./level3.hash.bin "Level 3 hash binary file") along with a [text file that contains the encrypted flag](./level3.flag.txt.enc "Level 3 encoded flag text file file"). It then prompts the user for a password, if the hashed password matches the hash stored in the binary file, it will decrypt the encrypted flag and print it out. The program also lists the seven possible passwords.

```python
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]
```
