# Trivial Flag Transfer Protocol

## Description

Figure out how they moved the [flag](https://mercury.picoctf.net/static/e4836d9bcc740d457f4331d68129a0bc/tftp.pcapng "Pico CTF link to download PCAP file").

## Hints

* What are some other ways to hide data?

## Walkthrough

After we download the [pcap](https://en.wikipedia.org/wiki/Pcap "Wikipedia article for pcap") file we can open it in [WireShark](https://en.wikipedia.org/wiki/Wireshark "Wikipedia article on WireShark").

![WireShark output for CTF pcap file](./Assets/wireshark-steps-1-of-3.png "WireShark output for CTF pcap file")

Looking through the output in the pcap file we'll notice that most of the network traffic uses the [Trivial File Transfer Protocol (TFTP)](https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol "Wikipedia article for TFTP"), a protocol used for simple file transferring. We'll also notice mentions of various files like the first entry which references a file called "instructions.txt".

We can extract these files by clicking ```File -> Export Objects -> TFTP```, then clicking ```Save All```.

![WireShark Dropdown Menu](./Assets/wireshark-steps-2-of-3.png "WireShark dropdown menu used to export objects from TFTP protocol")

![WireShark Popup](./Assets/wireshark-steps-3-of-3.png "Wireshark popup screen for saving all exported files")

After exporting the objects, we'll see the following files in our downloads folder.

* [instructions.txt](./Assets/instructions.txt "Instructions text file exported from pcap")

* [plan](./Assets/plan "Plan file exported from pcap")

* [program.deb](./Assets/program.deb "Deb file exported from pcap")

* [picture1.bmp](./Assets/picture1.bmp "First bitmap exported from pcap")

* [picture2.bmp](./Assets/picture2.bmp "Second bitmap exported from pcap")

* [picture3.bmp](./Assets/picture3.bmp "Third bitmap exported from pcap")

We'll start with the instructions file. Once opened, the file will show a long series of seemingly enciphered text.

```GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA```

Trying a bruteforce of all possible Caesar Cipher shifts on the enciphered text will reveal the key used is 13, making this a [ROT-13 cipher](https://en.wikipedia.org/wiki/ROT13 "Wikipedia article for ROT-13 cipher"). Once deciphered, the following text will be revealed.

```TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN```

After adding spaces:

```TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT AWAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN```

Since the instructions file mentions the plan file, we'll check there next.

```VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF```

Again we'll find enciphered text, maybe the developers used the same cipher used in the instructions file. After deciphering the text using ROT-13 we'll see the following text.

```IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS```

After adding spaces:

```I USED THE PROGRAM AND HID IT WITH - DUEDILIGENCE. CHECK OUT THE PHOTOS```

There's some important information revealed in this text. We have the program referenced and now we know the flag was hidden in the photos, the words due diligence also stick out as a possible tool name or password.

Next we'll move on to the [.deb file](https://www.lifewire.com/deb-file-2620596 "Lifewire article on deb files"). Deb files are Debian based software package files used for installing software, they typically contain two [tar files](https://www.howtogeek.com/362203/what-is-a-tar.gz-file-and-how-do-i-open-it/ "How to Geek article on tar files"): control.tar.gz and data.tar.gz. The control tar file contains metadata about the program like version number, dependencies, descriptions, etc. The data tar file contains the actual files needed by the program.

Extracting the contents of the [program.deb](./Assets/program.deb "program.deb file extracted using WireShark") file will see a folder named [program](./Assets/program/ "Program directory extracted from program.deb"), navigating to this folder we'll see the two tar files, [control.tar.gz](./Assets/program/control.tar.gz "Control tar file extracted from program.deb") and [data.tar.gz](./Assets/program/data.tar.xz "Data tar file extracted from program.deb"), along with a text file named [debian-binary](./Assets/program/debian-binary "debian-binary text file").

We'll skip [debian-binary](./Assets/program/debian-binary "debian-binary text file") because it's not important, and move straight to [control.tar.gz](./Assets/program/control.tar.gz "Control tar file extracted from program.deb"). Once extracted we'll see two files, one named [control](./Assets/control/control "Control text file extracted from control tar file") and the other [md5sums](./Assets/control/md5sums "MD5 sums for program files"). Reading either of these files will reveal to us the name of the tool used to hide the flag.

[control](./Assets/control/control "Control text file extracted from control tar file") (Program Metadata):

```
Package: steghide
Source: steghide (0.5.1-9.1)
Version: 0.5.1-9.1+b1
Architecture: amd64
Maintainer: Ola Lundqvist <opal@debian.org>
Installed-Size: 426
Depends: libc6 (>= 2.2.5), libgcc1 (>= 1:4.1.1), libjpeg62-turbo (>= 1:1.3.1), libmcrypt4, libmhash2, libstdc++6 (>= 4.9), zlib1g (>= 1:1.1.4)
Section: misc
Priority: optional
Description: A steganography hiding tool
 Steghide is steganography program which hides bits of a data file
 in some of the least significant bits of another file in such a way
 that the existence of the data file is not visible and cannot be proven.
 .
 Steghide is designed to be portable and configurable and features hiding
 data in bmp, wav and au files, blowfish encryption, MD5 hashing of
 passphrases to blowfish keys, and pseudo-random distribution of hidden bits
 in the container data.
```

[md5sums](./Assets/control/md5sums "MD5 sums for program files") (File Hashes)

```
71bdab1263ab4b8d28f34afa5f0ab121  usr/bin/steghide
11db80c2a5dbb9c6107853b08aeacc49  usr/share/doc/steghide/ABOUT-NLS.gz
57deb17212483b49f89587180d4d67d4  usr/share/doc/steghide/BUGS
72c7831222483f5c6d96ac2a8ca7ad48  usr/share/doc/steghide/CREDITS
adbb29f44a5e5eefda3c3d756cc15ab1  usr/share/doc/steghide/HISTORY
fe7cac39a1a1ef0975d24dfcf02f09b7  usr/share/doc/steghide/LEAME.gz
85587b9213ca2301eb450aad574d5f87  usr/share/doc/steghide/README.gz
a9e03fa8166b8fa918c81db1855b68d1  usr/share/doc/steghide/TODO
09d7710e276a06c4a3f3bc81b3b86a41  usr/share/doc/steghide/changelog.Debian.amd64.gz
e454b20fdc2208f8170e28b90b6d43f7  usr/share/doc/steghide/changelog.Debian.gz
1a2e10366a3a55d7a4cb5fc3c87a6bf7  usr/share/doc/steghide/changelog.gz
df8c0ea893b3f6f64a917824c6c9d224  usr/share/doc/steghide/copyright
fc53645374c583f11f628331be710d9a  usr/share/locale/de/LC_MESSAGES/steghide.mo
b8ceabc96f9bffd9157103e1a86be33f  usr/share/locale/es/LC_MESSAGES/steghide.mo
87ee9a19bb49b217dad67b5a889bb1d1  usr/share/locale/fr/LC_MESSAGES/steghide.mo
dbc3a8e974ccf7e91da81aca4a5c1605  usr/share/locale/ro/LC_MESSAGES/steghide.mo
921a5afd279097e4ed359ce3767068f5  usr/share/man/man1/steghide.1.gz
```

That's all the information we need to understand that the tool used to hide the flag within an image was the popular stegonagraphy tool known as 
[steghide](https://www.kali.org/tools/steghide/ "Kali Linux page for Steghide"). We can verify this by looking through the files in the data folder but it's not needed.


