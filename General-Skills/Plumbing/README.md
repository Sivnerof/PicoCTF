# Plumbing

## Description

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 7480.

## Hints

* Remember the flag format is picoCTF{XXXX}

* What's a pipe? No not that kind of pipe... [This kind](https://www.linfo.org/pipes.html "Linfo article on pipes")

## Walkthrough

```
$ nc jupiter.challenges.picoctf.org 7480 | grep "picoCTF"
picoCTF{digital_plumb3r_06e9d954}
^C
```
