# Hide Me

## Description

Every file gets a flag. The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/256/flag.png "Pico CTF link to download flag PNG").

## Hints

* (None)

## Walkthrough

After we download [flag.png](./flag.png "flag png file") from the link provided, we'll see the following image.

![flag png file](./flag.png "flag png file")

Taking a look at the metadata for the file we'll see a warning.

```
$ exiftool flag.png

File Name                       : flag.png
Directory                       : .
File Size                       : 42 KiB
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 512
Image Height                    : 504
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 512x504
Megapixels                      : 0.258
```

The warning informs us that the PNG has data after the [PNG IEND chunk](http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html "PNG specifications and standards with more information on IEND Chunk"). The PNG IEND chunk, according to PNG standards and specifications, should ALWAYS appear at the end of the data stream. Naturally, this alerts us to the fact that this file is more than meets the eye.

```
Warning                         : [minor] Trailer data after PNG IEND chunk
```

If we use the Linux strings command on the file we'll see, in the last two lines of the output, references to a directory called "secret" and a file named "flag.png".

```
$ strings flag.png

68-o
9uGB
YxAMa
TpvpC
secret/UT
secret/flag.pngUT
```

This PNG file clearly has embedded files, we can extract them using a tool like [BinWalk](https://www.kali.org/tools/binwalk/ "Kali docs for BinWalk").

The BinWalk syntax to carve embedded files is ```binwalk -e <file>```. If we run the command on our file we'll extract the "secret" directory and "flag.png" file we saw referenced in the output of our strings command.

```
$ binwalk -e flag.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2997, uncompressed size: 3152, name: secret/flag.png
43036         0xA81C          End of Zip archive, footer length: 22
```

After navigating to the ["secret" directory](./secret/ "Secret directory extracted from flag.png") we'll see the hidden "[flag.png](./flag.png "Secret flag file extracted from flag.png")" file, revealing our flag.

![Secret Flag](./secret/flag.png "Secret flag extracted from flag.png")

```picoCTF{Hiddinng_An_imag3_within_@n_ima9e_85e04ab8}```
