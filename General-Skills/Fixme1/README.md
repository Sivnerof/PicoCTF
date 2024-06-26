# Fixme1.py

## Description

Fix the syntax error in this Python script to print the flag. [Download Python script](https://artifacts.picoctf.net/c/25/fixme1.py "Pico CTF website link to download fixme1.py file")

## Hints

* Indentation is very meaningful in Python

* To view the file in the webshell, do: $ nano fixme1.py

* To exit nano, press Ctrl and x and follow the on-screen prompts.

* The str_xor function does not need to be reverse engineered for this challenge.

## Walkthrough

[Syntax errors](https://www.geeksforgeeks.org/what-is-a-syntax-error-and-how-to-solve-it/ "Geeks For Geeks article on syntax errors") are the most common errors in programming. Common syntax errors include misspelled variable or function names, improper or missing indentation, forgotten parentheses, unmatched quotes, etc.

A quick way to find the syntax error in the Python program provided to us, is to simply run the program and see what error is returned by the Python interpreter. Keep in mind that running unfamiliar programs can be dangerous, especially if the file is malicious.

If we run the program, we'll see an error that informs us that line 20 of the code contains an unexpected indent.

```
$ python3 fixme1.py
  File "fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
```

Looking at the Python code we'll see the line referenced in the error all the way at the end.

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


flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5a) + chr(0x07) + chr(0x00) + chr(0x46) + chr(0x0b) + chr(0x1a) + chr(0x5a) + chr(0x1d) + chr(0x1d) + chr(0x2a) + chr(0x06) + chr(0x1c) + chr(0x5a) + chr(0x5c) + chr(0x55) + chr(0x40) + chr(0x3a) + chr(0x58) + chr(0x0a) + chr(0x5d) + chr(0x53) + chr(0x43) + chr(0x06) + chr(0x56) + chr(0x0d) + chr(0x14)

  
flag = str_xor(flag_enc, 'enkidu')
  print('That is correct! Here\'s your flag: ' + flag)


```

After deindenting the print statement, our code should look like this:

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


flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5a) + chr(0x07) + chr(0x00) + chr(0x46) + chr(0x0b) + chr(0x1a) + chr(0x5a) + chr(0x1d) + chr(0x1d) + chr(0x2a) + chr(0x06) + chr(0x1c) + chr(0x5a) + chr(0x5c) + chr(0x55) + chr(0x40) + chr(0x3a) + chr(0x58) + chr(0x0a) + chr(0x5d) + chr(0x53) + chr(0x43) + chr(0x06) + chr(0x56) + chr(0x0d) + chr(0x14)

  
flag = str_xor(flag_enc, 'enkidu')
print('That is correct! Here\'s your flag: ' + flag)

```

If we run the program with the syntax error fixed, we'll see that the output of the program is the flag needed to solve this challenge.

```
$ python3 fixed.py
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_6a476c8f}
```

```picoCTF{1nd3nt1ty_cr1515_6a476c8f}```
