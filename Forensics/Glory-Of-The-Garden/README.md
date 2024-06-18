# Glory of the Garden

## Description

[This garden](https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg "Pico CTF link to download image of a garden") contains more than it seems.

## Hints

* What is a hex editor?

## Walkthrough

After downloading the image provided, we'll see a photo of a garden with a trail that runs through it. Although it looks like an ordinary image we know there is a flag hidden here somewhere.

![Garden Trail](./garden.jpg "A trail runs through the middle of a garden")

There are many tools commonly used in image steganography, but for this task, we'll only need one: ```strings```.

The Linux ```strings``` command looks for sequences of printable characters found within files, by default it prints out any strings that are 4 characters or longer. This can be changed by providing ```-n``` as an argument with the new number, but for this challenge it won't be necessary.

If we run the ```strings``` command on the [garden.jpg](./garden.jpg "Garden image needed for CTF") file, we'll find the hidden flag towards the end of the output.

```
$ strings garden.jpg

[...REDACTED FOR BREVITY...]

M(.I
]hWP&
jc#k
=7g&
mjx/
s\]|."Ue
\qZf
Here is a flag "picoCTF{more_than_m33ts_the_3y3657BaB2C}"
```

```picoCTF{more_than_m33ts_the_3y3657BaB2C}```
