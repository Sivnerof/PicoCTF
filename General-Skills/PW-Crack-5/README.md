# PW Crack 5

## Description

Can you crack the password to get the flag? Download the password checker [here]( "PicoCTF link to download PW Crack level 5 password checker program") and you'll need the encrypted [flag]( "PicoCTF link to download PW Crack level 5 encrypted flag text file") and the [hash]( "PicoCTF link to download PW Crack level 5 hash binary file") in the same directory too. Here's a [dictionary]( "PicoCTF link to download PW Crack level 5 password wordlist") with all possible passwords based on the password conventions we've seen so far.

## Hints

* Opening a file in Python is crucial to using the provided dictionary.

* You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, strip

* The str_xor function does not need to be reverse engineered for this challenge.

## Walkthrough

[Level 5 encoded flag text file file](./level5.flag.txt.enc "Level 5 encoded flag text file file")

[Level 5 hash binary file](./level5.hash.bin "Level 5 hash binary file")

[Level 5 python password checker program](./level5.py "Level 5 python password checker program")

[Password Dictionary](./dictionary.txt "Password Dictionary")
