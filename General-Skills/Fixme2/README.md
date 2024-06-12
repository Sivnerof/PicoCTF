# Fixme2.py

## Description

Fix the syntax error in the Python script to print the flag. [Download Python script](https://artifacts.picoctf.net/c/6/fixme2.py "Pico CTF link to download python file")

## Hints

* Are equality and assignment the same symbol?

* To view the file in the webshell, do: $ nano fixme2.py

* To exit nano, press Ctrl and x and follow the on-screen prompts.

* The str_xor function does not need to be reverse engineered for this challenge.

## Walkthrough

[Syntax errors](https://www.geeksforgeeks.org/what-is-a-syntax-error-and-how-to-solve-it/ "Geeks For Geeks article on syntax errors") are the most common errors in programming. Common syntax errors include misspelled variable or function names, improper or missing indentation, forgotten parentheses, unmatched quotes, etc.

A quick way to find the syntax error in the Python program provided to us, is to simply run the program and see what error is returned by the Python interpreter. Keep in mind that running unfamiliar programs can be dangerous, especially if the file is malicious.

If we run the program, we'll see an error that informs us that line 22 of the code contains a syntax error.

```
$ python3 fixme2.py
  File "/home/sivnerof/Code/Pico-CTF/General-Skills/Fixme2/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

The syntax error thrown back by the Python interpretor in this case is very specific, letting us know that maybe we made an error in our equality check.

```
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

If we review the given code, we can quickly verify that this is indeed the case.

```python
import random



def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])


flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x58) + chr(0x18) + chr(0x11) + chr(0x41) + chr(0x09) + chr(0x5f) + chr(0x1f) + chr(0x10) + chr(0x3b) + chr(0x1b) + chr(0x55) + chr(0x1a) + chr(0x34) + chr(0x5d) + chr(0x51) + chr(0x40) + chr(0x54) + chr(0x09) + chr(0x05) + chr(0x04) + chr(0x57) + chr(0x1b) + chr(0x11) + chr(0x31) + chr(0x0d) + chr(0x5f) + chr(0x05) + chr(0x40) + chr(0x04) + chr(0x0b) + chr(0x0d) + chr(0x0a) + chr(0x19)

  
flag = str_xor(flag_enc, 'enkidu')

# Check that flag is not empty
if flag = "":
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)


```

The equality check uses single equals signs instead of double equals.

```python
if flag = "":
  print('String XOR encountered a problem, quitting.')
```

In Python we check for equality using the double equals signs, ```==```, while the single equals sign, ```=```, is used for assignment. For example, to say that the variable named ```testing``` is equal to ```5```, we say ```testing = 5```. On the other hand, if we want to ask whether testing is equal to 5 we would do ```testing == 5```. Since the code above makes more sense asking if ```flag == ""```, it's safe to assume the error is in the incorrect use of equality operators. Addind one more equals sign seems to fix the problem.

```python
import random

def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])


flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x58) + chr(0x18) + chr(0x11) + chr(0x41) + chr(0x09) + chr(0x5f) + chr(0x1f) + chr(0x10) + chr(0x3b) + chr(0x1b) + chr(0x55) + chr(0x1a) + chr(0x34) + chr(0x5d) + chr(0x51) + chr(0x40) + chr(0x54) + chr(0x09) + chr(0x05) + chr(0x04) + chr(0x57) + chr(0x1b) + chr(0x11) + chr(0x31) + chr(0x0d) + chr(0x5f) + chr(0x05) + chr(0x40) + chr(0x04) + chr(0x0b) + chr(0x0d) + chr(0x0a) + chr(0x19)


flag = str_xor(flag_enc, 'enkidu')

# Check that flag is not empty
if flag == "":
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)
```

