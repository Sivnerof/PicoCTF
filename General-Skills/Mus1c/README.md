# Mus1c

## Description

I wrote you a [song](https://jupiter.challenges.picoctf.org/static/c594d8d915de0129d92b4c41e25a2313/lyrics.txt "Pico CTF link to download lyrics text file"). Put it in the picoCTF{} flag format.

## Hints

* Do you think you can master rockstar?

## Walkthrough

Looking at the [lyrics.txt](./lyrics.txt "Lyrics text file") file we'll see what looks like a very poorly written song. In reality, these are lines of code for an [esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language "Wikipedia article for esoteric programming languages") known as [Rockstar](https://codewithrockstar.com/ "Rockstar programming language official website") written by [Dylan Beattie](https://dylanbeattie.net/ "Dylan Beattie").

```
Pico's a CTFFFFFFF
my mind is waitin
It's waitin

Put my mind of Pico into This
my flag is not found
put This into my flag
put my flag into Pico


shout Pico
shout Pico
shout Pico

My song's something
put Pico into This

Knock This down, down, down
put This into CTF

shout CTF
my lyric is nothing
Put This without my song into my lyric
Knock my lyric down, down, down

shout my lyric

Put my lyric into This
Put my song with This into my lyric
Knock my lyric down

shout my lyric

Build my lyric up, up ,up

shout my lyric
shout Pico
shout It

Pico CTF is fun
security is important
Fun is fun
Put security with fun into Pico CTF
Build Fun up
shout fun times Pico CTF
put fun times Pico CTF into my song

build it up

shout it
shout it

build it up, up
shout it
shout Pico
```

Pasting the lyrics into the [Rockstar interpreter](https://codewithrockstar.com/online "Rockstar interpreter"), we'll find that the program outputs a series of numbers.

```
114
114
114
111
99
107
110
114
110
48
49
49
51
114
```

Converting the numbers from decimal to ASCII reveals the following.

```rrrocknrn0113r```

Placing the text in flag format and hitting submit solves the challenge.

```picoCTF{rrrocknrn0113r}```
