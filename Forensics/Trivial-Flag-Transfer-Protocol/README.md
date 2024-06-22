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

