# So Meta

## Description

Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/00efdf2961da1e21470ffc0d496c3cc2/pico_img.png "Pico CTF link to download challenge image").

## Hints

* What does meta mean in the context of files?

* Ever heard of metadata?

## Walkthrough

This challenge can be completed fairly quickly and should be pretty easy to figure out. If we download the file named [pico_img.png](./pico_img.png "So Meta challenge image"), we'll see the following image.

![So Meta Challenge Image](./pico_img.png "So Meta challenge image")

Looking through the image metadata by using a tool like [ExifTool](https://en.wikipedia.org/wiki/ExifTool "Wikipedia page for ExifTool"), we'll see that one of the fields sticks out.

```
$ exiftool pico_img.png

File Name                       : pico_img.png
Directory                       : .
File Size                       : 106 KiB
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{s0_m3ta_fec06741}
Image Size                      : 600x600
Megapixels                      : 0.360
```

The artist field in the metadata contains the flag.

```
Artist                          : picoCTF{s0_m3ta_fec06741}
```

```picoCTF{s0_m3ta_fec06741}```
