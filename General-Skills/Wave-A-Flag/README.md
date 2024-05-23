# Wave A Flag

## Description

Can you invoke help flags for a tool or binary? [This program](./warm "") has extraordinarily helpful information...

## Hints

* This program will only work in the webshell or another Linux computer.

* To get the file accessible in your shell, enter the following in the Terminal prompt: ```$ wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm```

* Run this program by entering the following in the Terminal prompt: ```$ ./warm```, but you'll first have to make it executable with ```$ chmod +x warm```

* ```-h``` and ```--help``` are the most common arguments to give to programs to get more information from them!

* Not every program implements help features like ```-h``` and ```--help```.

## Walkthrough

This challenge is fairly simple, we're given an executable and asked if we know how to "invoke help flags" for tools or binaries. Typically this is done by providing ```-h``` or ```--help``` as a command line argument to a program. In order to run the program given to us, named [warm](./warm "Warm Binary"), we first need to grant it the proper [permissions](https://linuxhandbook.com/linux-file-permissions/ "Linux File Permissions").

Linux file permissions can be changed by using the [chmod](https://linuxize.com/post/chmod-command-in-linux/ "Linuxize article on the chmod command") (change mode) command followed by an option such as ```+x``` (add execute permissions for all users) and the file name.

Example: ```$ chmod +x warm```

After we have given execute permissions to the file we can run it.

```
$ ./warm
Hello user! Pass me a -h to learn what I can do!
```

Now that we made sure it runs we can provide the help option to receive the flag hidden within the program.

```
$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
```
