# Secret of the Polyglot

## Description

The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file? Download the suspicious file [here](https://artifacts.picoctf.net/c_titan/7/flag2of2-final.pdf "Pico CTF link to download challenge file").

## Hints

* This problem can be solved by just opening the file in different ways

## Walkthrough

If we download the file given to us, named [flag2of2-final.pdf](./flag2of2-final.pdf "Suspicious PDF file"), we'll see that it contains the text: ```1n_pn9_&_pdf_53b741d6}```.

This file at first glance appears to be a simple PDF that contains half of the flag needed to solve this challenge. But if we use the [Linux file command](https://www.geeksforgeeks.org/file-command-in-linux-with-examples/ "Geeks For Geeks article on Linux file command") on the "PDF", we'll see that Linux claims this file is actually a PNG.


```
$ file flag2of2-final.pdf
flag2of2-final.pdf: PNG image data, 50 x 50, 8-bit/color RGBA, non-interlaced
```

If we use [ExifTool](https://en.wikipedia.org/wiki/ExifTool "Wikipedia page for ExifTool") on the file, we'll see that it also registers this file as a PNG, and the metadata provides a lot of evidence supporting this.

```
$ exiftool flag2of2-final.pdf
ExifTool Version Number         : 12.40
File Name                       : flag2of2-final.pdf
Directory                       : .
File Size                       : 3.3 KiB
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 50
Image Height                    : 50
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Profile Name                    : ICC profile
Profile CMM Type                : Little CMS
Profile Version                 : 4.3.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : GIMP built-in sRGB
Profile Copyright               : Public Domain
Media White Point               : 0.9642 1 0.82491
Chromatic Adaptation            : 1.04788 0.02292 -0.05022 0.02959 0.99048 -0.01707 -0.00925 0.01508 0.75168
Red Matrix Column               : 0.43604 0.22249 0.01392
Blue Matrix Column              : 0.14305 0.06061 0.71393
Green Matrix Column             : 0.38512 0.7169 0.09706
Chromaticity Channels           : 3
Chromaticity Colorant           : Unknown (0)
Chromaticity Channel 1          : 0.64 0.33002
Chromaticity Channel 2          : 0.3 0.60001
Chromaticity Channel 3          : 0.15001 0.06
Device Mfg Desc                 : GIMP
Device Model Desc               : sRGB
Pixels Per Unit X               : 11811
Pixels Per Unit Y               : 11811
Pixel Units                     : meters
Comment                         : Created with GIMP
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 50x50
Megapixels                      : 0.003
```

If we look at the exiftool output, we'll even see a warning alerting us that the PNG has data after the [PNG IEND chunk](http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html "PNG specifications and standards with more information on IEND Chunk"). The PNG IEND chunk, according to PNG standards and specifications, should ALWAYS appear at the end of the data stream. Naturally, this alerts us to the fact that this file is more than meets the eye.

```
Warning                         : [minor] Trailer data after PNG IEND chunk
```

If we use the Linux strings command on the file and look at the strings found after "IEND" we'll see that after the PNG ends a whole bunch of PDF data begins.

A better way to do this would be to print the files hexdump with the [Linux xxd command](https://linuxhandbook.com/xxd-command/ "Linux handbook article on Linux xxd command"), where we'll find that after the IEND chunk we can find the [file signature](https://en.wikipedia.org/wiki/List_of_file_signatures "Wikipedia page for file signatures") for a PDF file.

PDF File Signature: ```25 50 44 46 2D 	%PDF-```

```
$ xxd flag2of2-final.pdf

[...REMOVED FOR BREVITY...]
00000380: 0f86 f099 66ec 0000 0000 4945 4e44 ae42  ....f.....IEND.B
00000390: 6082 2550 4446 2d31 2e34 0a25 c7ec 8fa2  `.%PDF-1.4.%....
[...REMOVED FOR BREVITY...]
```

Now we know what this file is: it's both a PNG and a PDF. These types of files are known as [polyglot files](https://en.wikipedia.org/wiki/Polyglot_(computing) "Wikipedia article on polyglot files") because they are written in several different syntaxes, languages, or file formats. This makes them perfect for evading detection and bypassing security measures by tricking software into misidentifying file types and potentially executing malicious code.

If we take the [flag2of2-final.pdf](./flag2of2-final.pdf "Suspicious PDF file") and change the file extension to png, we should be able to collect the second piece of the flag.

[flag2of2-final.png](./flag2of2-final.png "PDF file after changing file extension to png"):

![Polyglot PNG](./flag2of2-final.png "PDF file after changing file extension to png")

```picoCTF{f1u3n7_```

Putting this piece of the flag together with the one we found in the PDF file leaves us with:

```picoCTF{f1u3n7_1n_pn9_&_pdf_53b741d6}```
