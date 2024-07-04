# Can You See

## Description

How about some hide and seek? Download this file [here](https://artifacts.picoctf.net/c_titan/130/unknown.zip "Pico CTF link to download mysterious zip file").

## Hints

* How can you view the information about the picture?

* If something isn't in the expected form, maybe it deserves attention?

## Walkthrough

Unzipping [unknown.zip](./unknown.zip "Mysterious zip file") and navigating to the [unknown directory](./unknown/ "Unknown directory unzipped from unknown.zip") will reveal an image named [ukn_reality.jpg](./unknown/ukn_reality.jpg "Image extracted from unknown zip file").

![Ukn Reality Image](./unknown/ukn_reality.jpg "Image extracted from unknown zip file")

Since we know nothing about the file, a good place to start is reviewing the metadata. This can be done with a tool like [ExifTool](https://en.wikipedia.org/wiki/ExifTool "Wikipedia page for ExifTool").

```
$ exiftool ukn_reality.jpg

File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.2 MiB
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
```

Reviewing the metadata, nothing seems out of the ordinary until we get to the field for the "Attribution URL" which is encoded in what appears to be Base-64. Immediately this strikes us as suspicious. What is encoded data doing in a field designed for straight-forward URL's?

```
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==
```

Decoding the string from Base-64 reveals the hidden flag.

```
$ echo -n 'cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==' | base64 --decode

picoCTF{ME74D47A_HIDD3N_6a9f5ac4}
```
