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

We can write a simple python script that hashes all possible passwords and compares them to the correct password hash but there's a faster way we can find the right password.

If we use the [xxd Linux command](https://www.geeksforgeeks.org/xxd-command-in-linux/ "Geeks For Geeks article on xxd Linux command") to print out a hexdump of the [level3.hash.bin file](./level3.hash.bin "Level 3 hash binary file"), we can grab the hashed password.

```
$ xxd level3.hash.bin
00000000: 1602 6d60 ff9b 5441 0b34 35b4 03af d226  ..m`..TA.45....&
```

Hash from hexdump:

```1602 6d60 ff9b 5441 0b34 35b4 03af d226```

Hash from hexdump after removing spaces:

```16026d60ff9b54410b3435b403afd226```

Now that we have the correct password hash we can use a [hash decryptor](https://hashes.com/en/decrypt/hash "Online hash decryptor from Hashes.com") to get the original password.

```16026d60ff9b54410b3435b403afd226:2295```

After decrypting the correct password hash we'll see that the password used was ```2295```. Running the Python program with the newly found password will reveal the flag.

```
$ python3 level3.py
Please enter correct password for flag: 2295
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_6f98a49f}
```

```picoCTF{m45h_fl1ng1ng_6f98a49f}```
