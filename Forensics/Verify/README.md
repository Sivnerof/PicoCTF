# Verify

## Description

People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate. You can download the challenge files here:

* [challenge.zip](https://artifacts.picoctf.net/c_rhea/20/challenge.zip "Pico CTF link to download challenge files")

The same files are accessible via SSH.

* Checksum: fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7

* To decrypt the file once you've verified the hash, run ```./decrypt.sh files/<file>```.

## Hints

* Checksums let you tell if a file is complete and from the original distributor. If the hash doesn't match, it's a different file.

* You can create a SHA checksum of a file with ```sha256sum <file>``` or all files in a directory with ```sha256sum <directory>/*```.

* Remember you can pipe the output of one command to another with ```|```. Try practicing with the 'First Grep' challenge if you're stuck!

## Walkthrough

At the beginning of this challenge we're given the sha-256 hash of the flag file (fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7). We're also given a bunch of files, so manually looking for the flag will be a bit tedious. Instead we can use the ```sha256sum``` command on all files in the ```./files``` directory to get the sha-256 hashes of every file. We can do this by using the command ```sha256sum ./files/*```. Since we're only looking for the hash that starts with ```fba9f```, we can pipe the output of the previous command to ```grep```. The full command should look like this: ```sha256sum ./files/* | grep fba9f```.

```
$ sha256sum ./files/* | grep fba9f
fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7  ./files/87590c24
```

The output of the command above shows that the file named [87590c24](./challenge/home/ctf-player/drop-in/files/87590c24 "Encrypted flag text file") hashes to the checksum we're looking for.

Next, we run the ```decrypt.sh``` program on ```./files/87590c24``` to get the flag.

```
ctf-player@pico-chall$ ./decrypt.sh ./files/87590c24
picoCTF{trust_but_verify_87590c24}
```
