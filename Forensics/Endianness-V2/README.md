# Endianness V2

## Description

Here's a file that was recovered from a 32-bits system that organized the bytes a weird way. We're not even sure what type of file it is. Download it [here](https://artifacts.picoctf.net/c_titan/112/challengefile "Pico CTF link to download challenge file") and see what you can get out of it.

## Hints

* (None)

## Walkthrough

All we know about the file named "[challengefile](./challengefile "Mysterious file")" is that it came from a 32-bit system that "organized the bytes in a weird way". The title of the room hints that the problem relates to [endianness](https://www.freecodecamp.org/news/what-is-endianness-big-endian-vs-little-endian/ "freeCodeCamp article on little and big endian").

If you're unfamiliar with [endianness](https://www.freecodecamp.org/news/what-is-endianness-big-endian-vs-little-endian/ "freeCodeCamp article on little and big endian"), you should start with [version 1 of this challenge](https://play.picoctf.org/practice/challenge/414 "Pico CTF endianness challenge") and read the [write-up I did for that one](../../General-Skills/Endianness/ "Endianness V1 writeup"). Since this challenge is the second part in a series of endianness challenges and rated medium difficulty, I'll assume you're already familiar.

If we run the Linux "file" command on "[challengefile](./challengefile "Mysterious file")" we'll see that Linux classifies this file as "data".

```
$ file challengefile
challengefile: data
```

Viewing the metadata won't be helpful either, giving us a warning that the file contains JPEG-like data with an unknown 1-byte header, indicating that the data might be corrupted or misinterpreted.

```
$ exiftool challengefile

File Name                       : challengefile
Directory                       : .
File Size                       : 3.3 KiB
File Permissions                : -rw-rw-r--
Warning                         : Processing JPEG-like data after unknown 1-byte header
```

Our next step is to view a hexdump of the file and see if we can get an idea of what's going on.

```
$ xxd challengefile
00000000: e0ff d8ff 464a 1000 0100 4649 0100 0001  ....FJ....FI....
00000010: 0000 0100 4300 dbff 0606 0800 0805 0607  ....C...........
00000020: 0907 0707 0c0a 0809 0b0c 0d14 1219 0c0b  ................
[...REMOVED FOR BREVITY...]
```

The first two bytes in the hexdump are "e0" and "ff". If we look these up on a [list of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures "List of file signatures on Wikipedia"), we won't find any matching file type. Remembering that endianness sometimes uses a reverse order than what we're used to, we can try searching for these bytes in reverse order. Searching the list for "ff e0", instead of "e0 ff", does return a match for a JPEG file signature.

JPEG File Signature:
```FF D8 FF E0 00 10 4A 46 49 46 00 01```

You'll also notice that every byte in the JPEG file signature can be found in the first line of the hex dump, just out of order. Instead of ```FF D8 FF E0``` we get ```E0 FF D8 FF```. You'll see this pattern repeat every four bytes, which makes sense because the room description states this file came from a 32-bit (4 bytes) system.

| **BYTE NUMBER** | **CHALLENGEFILE HEXDUMP** | **JPEG FILE SIGNATURE** |
|:---------------:|:-------------------------:|:-----------------------:|
| 1               | E0 FF D8 FF               | FF D8 FF E0             |
| 2               | 46 4A 10 00               | 00 10 4A 46             |
| 3               | 01 00 46 49               | 49 46 00 01             |

If we can reverse the byte order every four bytes we should be able to recover the original file.


* UNFINISHED WRITEUP TO THIS POINT
* UNFINISHED WRITEUP TO THIS POINT
* UNFINISHED WRITEUP TO THIS POINT
* UNFINISHED WRITEUP TO THIS POINT
* UNFINISHED WRITEUP TO THIS POINT
* UNFINISHED WRITEUP TO THIS POINT


```python
chunk_size = 4

f = open("challengefile", mode="rb")
f2 = open("challengefilereversed", mode="wb")

while True:
    chunk = f.read(chunk_size)
    if not chunk:
        break
    bytes_reversed = chunk[::-1]
    f2.write(bytes_reversed)

f.close()
f2.close()
```
