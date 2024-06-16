# PW Crack 1

## Description

Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/12/level1.py "Pico CTF link for Python password checker program") and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/12/level1.flag.txt.enc "Pico CTF link for encrypted flag text file") in the same directory too.

## Hints

* To view the file in the webshell, do: $ nano level1.py

* To exit nano, press Ctrl and x and follow the on-screen prompts.

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


flag_enc = open('level1.flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "8713"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()

```

While scanning through the code, the function named ```level_1_pw_check``` stands out.

```python
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "8713"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```

It seems that the program takes an encrypted flag found in the text file named [level1.flag.txt.enc](./level1.flag.txt.enc "Encrypted flag text file") and will print it out after decrypting it, but only if the password provided is equal to ```8713```.

```python
if( user_pw == "8713"):
    print("Welcome back... your flag, user:")
    decryption = str_xor(flag_enc.decode(), user_pw)
    print(decryption)
    return
```

Knowing this, we can run the program and when it prompts us for the password we can provide ```8713``` as the input. The program should then output the CTF flag.

```
$ python3 level1.py
Please enter correct password for flag: 8713
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_1b2fd683}
```

```picoCTF{545h_r1ng1ng_1b2fd683}```
