# ASCII FTW

## Description

This program has constructed the flag using hex ascii values. Identify the flag text by disassembling the program. You can download the file from [here](https://artifacts.picoctf.net/c/507/asciiftw "Pico CTF link to download ASCII FTW binary").

## Hints

* The combined range of hex-ascii for English alphabets and numerical digits is from 30 to 7A.

* Online hex-ascii converters can be helpful.

## Walkthrough

After we download the binary file, [asciiftw](./asciiftw "ASCII FTW binary program"), we'll need to open it in a disassembler like [Ghidra](https://ghidra-sre.org/ "Official website for the reverse engineering tool GHIDRA") or [IDA](https://hex-rays.com/ida-free/ "Official website for the reverse engineering tool IDA") to analyze its code and understand its functionality.

Once we load the program into the disassembler, we'll see a simple program where hexadecimal values are being loaded into memory.

![ASCII characters shown in disassembler](./ascii-characters-shown-in-disassembler.png "ASCII characters shown in disassembler")

```
mov     [rbp+var_30], 70h ; 'p'
mov     [rbp+var_2F], 69h ; 'i'
mov     [rbp+var_2E], 63h ; 'c'
mov     [rbp+var_2D], 6Fh ; 'o'
mov     [rbp+var_2C], 43h ; 'C'
mov     [rbp+var_2B], 54h ; 'T'
mov     [rbp+var_2A], 46h ; 'F'
mov     [rbp+var_29], 7Bh ; '{'
mov     [rbp+var_28], 41h ; 'A'
mov     [rbp+var_27], 53h ; 'S'
mov     [rbp+var_26], 43h ; 'C'
mov     [rbp+var_25], 49h ; 'I'
mov     [rbp+var_24], 49h ; 'I'
mov     [rbp+var_23], 5Fh ; '_'
mov     [rbp+var_22], 49h ; 'I'
mov     [rbp+var_21], 53h ; 'S'
mov     [rbp+var_20], 5Fh ; '_'
mov     [rbp+var_1F], 45h ; 'E'
mov     [rbp+var_1E], 41h ; 'A'
mov     [rbp+var_1D], 53h ; 'S'
mov     [rbp+var_1C], 59h ; 'Y'
mov     [rbp+var_1B], 5Fh ; '_'
mov     [rbp+var_1A], 37h ; '7'
mov     [rbp+var_19], 42h ; 'B'
mov     [rbp+var_18], 43h ; 'C'
mov     [rbp+var_17], 44h ; 'D'
mov     [rbp+var_16], 39h ; '9'
mov     [rbp+var_15], 37h ; '7'
mov     [rbp+var_14], 31h ; '1'
mov     [rbp+var_13], 44h ; 'D'
mov     [rbp+var_12], 7Dh ; '}'
```

Taking the ASCII representations of these hexadecimal values and putting them together reveals our flag.

```picoCTF{ASCII_IS_EASY_7BCD971D}```
