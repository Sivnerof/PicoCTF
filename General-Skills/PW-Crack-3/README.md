# PW Crack 3

## Description

Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/18/level3.py "PicoCTF link to download PW Crack level 3 password checker program") and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/18/level3.flag.txt.enc "PicoCTF link to download PW Crack level 3 encrypted flag text file") and the [hash](https://artifacts.picoctf.net/c/18/level3.hash.bin "PicoCTF link to download PW Crack level 3 hash binary file") in the same directory too. There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## Hints

* To view the level3.hash.bin file in the webshell, do: $ bvi level3.hash.bin

* To exit bvi type :q and press enter.

* The str_xor function does not need to be reverse engineered for this challenge.

## Walkthrough

[Level 3 encoded flag text file file](./level3.flag.txt.enc "Level 3 encoded flag text file file")

[Level 3 hash binary file](./level3.hash.bin "Level 3 hash binary file")

[Level 3 python password checker program](./level3.py "Level 3 python password checker program")
