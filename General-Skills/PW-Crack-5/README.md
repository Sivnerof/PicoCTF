# PW Crack 5

## Description

Can you crack the password to get the flag? Download the password checker [here]( "PicoCTF link to download PW Crack level 5 password checker program") and you'll need the encrypted [flag]( "PicoCTF link to download PW Crack level 5 encrypted flag text file") and the [hash]( "PicoCTF link to download PW Crack level 5 hash binary file") in the same directory too. Here's a [dictionary]( "PicoCTF link to download PW Crack level 5 password wordlist") with all possible passwords based on the password conventions we've seen so far.

## Hints

* Opening a file in Python is crucial to using the provided dictionary.

* You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, strip

* The str_xor function does not need to be reverse engineered for this challenge.

## Walkthrough

If we open the [Level 5 python password checker program](./level5.py "Level 5 python password checker program") we'll see the following code.

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

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_5_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_5_pw_check()

```

The Python program takes a [binary file that contains a hashed password](./level5.hash.bin "Level 5 hash binary file") along with a [text file that contains the encrypted flag](./level5.flag.txt.enc "Level 5 encoded flag text file file"). It then prompts the user for a password, if the hashed password matches the hash stored in the binary file, it will decrypt the encrypted flag and print it out.

We're also given a [wordlist of potential passwords](./dictionary.txt "Password Dictionary").