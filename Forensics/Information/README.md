# Information

## Description

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](./cat.jpg "Photo of a cat lounging on a laptop")

## Hints

* Look at the details of the file

* Make sure to submit the flag as picoCTF{XXXXX}

## Walkthrough

When dealing with forensics of an image a good place to start is reviewing any [image metadata](https://www.techtarget.com/whatis/definition/image-metadata "Tech Target Article On Image Metadata"). Metadata is information that has been embedded into an image, this can be things like the creation date, modification date, copyright information, location where the photo was taken, width, size, as well as adding any other information a user wants. For example a user could add a field called foobar with a value of baz. One of the most common tools for viewing image metadata is [exiftool](https://en.wikipedia.org/wiki/ExifTool "Exiftool Wikipedia").

Using [exiftool](https://en.wikipedia.org/wiki/ExifTool "Exiftool Wikipedia") on [cat.jpg](./cat.jpg "Photo of a cat lounging on a laptop") shows the following.

```
$ exiftool cat.jpg
ExifTool Version Number         : 12.40
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 KiB
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

One of the fields found within the images metadata should stand out. The ```License``` field seems to have an encoded value (```cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9```) which looks similar to Base-64.

Decoding ```cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9``` from Base-64 reveals the flag ```picoCTF{the_m3tadata_1s_modified}```
