# What's A Net Cat

## Description

Using netcat (nc) is going to be pretty important. Can you connect to jupiter.challenges.picoctf.org at port 64287 to get the flag?

## Hints

[nc tutorial](https://linux.die.net/man/1/nc "Netcat Tutorial")

## Walkthrough

Netcat is a networking tool commonly used to receive and transmit data using TCP or UDP.

If we connect to port ```64287``` on ```jupiter.challenges.picoctf.org``` by using the command ```nc jupiter.challenges.picoctf.org 64287``` we'll receive the following flag.

```
$ nc jupiter.challenges.picoctf.org 64287
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_284be8f7}
```