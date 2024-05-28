# The Numbers

## Description

The [numbers](./the_numbers.png "Series of enciphered numbers")... what do they mean?

## Hints

* The flag is in the format PICOCTF{}

## Walkthrough

![Series of enciphered numbers](./the_numbers.png "Series of enciphered numbers")

Fun fact, the quote used in the CTF description ("The numbers... what do they mean?") is a reference to dialogue from [Alex Mason](https://callofduty.fandom.com/wiki/Alex_Mason "Call of Duty Wiki article for Alex Mason")'s interrogation scene in [Call of Duty: Black Ops](https://en.wikipedia.org/wiki/Call_of_Duty%3A_Black_Ops "Wikipedia article for Call of Duty: Black Ops"). You can watch the scene on YouTube by clicking [this link](https://www.youtube.com/watch?v=vVPT0JT1dOw "Alex Mason's interrogation on YouTube - The numbers Mason, what do they mean?")

Encoded text: ```16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14}```

Looking at the numbers for any clues you might notice that they all lie within the range of 1-26. Since there are 26 letters in the English alphabet, this suggests the use of an [A1Z26 cipher](https://www.dcode.fr/letter-number-cipher "Dcode article and decoder/encoder for A1Z26 Cipher"). The A1Z26 Cipher is a simple cipher where A = 1, B =2, ..., Z = 26, hence the name A1Z26, essentially every character is replaced with its numeric position.

Deciphering this code is so simple it can be done manually using the table below, or an online tool like [Dcode's A1Z26 Decoder/Encoder](https://www.dcode.fr/letter-number-cipher "Dcode article and decoder/encoder for A1Z26 Cipher").

| **LETTER** | **POSITION** |
|:----------:|:------------:|
| A          | 1            |
| B          | 2            |
| C          | 3            |
| D          | 4            |
| E          | 5            |
| F          | 6            |
| G          | 7            |
| H          | 8            |
| I          | 9            |
| J          | 10           |
| K          | 11           |
| L          | 12           |
| M          | 13           |
| N          | 14           |
| O          | 15           |
| P          | 16           |
| Q          | 17           |
| R          | 18           |
| S          | 19           |
| T          | 20           |
| U          | 21           |
| V          | 22           |
| W          | 23           |
| X          | 24           |
| Y          | 25           |
| Z          | 26           |


Decoded Text: ```PICOCTF{THENUMBERSMASON}```
