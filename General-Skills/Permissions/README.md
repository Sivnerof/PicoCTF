# Permissions

## Description

Can you read files in the root file?

Additional details will be available after launching your challenge instance.

## Hints

What permissions do you have?

## Walkthrough

After connecting to the target machine via ssh we'll be dropped into the home directory of "picoplayer", a low privilege user. Our goal is [vertical escalation](https://en.wikipedia.org/wiki/Privilege_escalation "Wikipedia article on privilege escalation"), so we should check if "picoplayer" has any sudo privileges. We can do this by using the command ```sudo -l```, which will list all sudo privileges for the current user.
```

$ sudo -l
[sudo] password for picoplayer: 
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
```

Looking through the output for ```sudo -l```, we'll see that "picoplayer" can run [vi](https://www.geeksforgeeks.org/vi-editor-unix/ "Geeks For Geeks article on Vi text editor") as any user (ALL).

```
User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
```

Our next step is to use the vi text editor to check the ```/root``` directory. We can do this with the command ```sudo vi /root``` which will output the following.

```
../
./
.vim/
.bashrc
.flag.txt
.profile
.viminfo
```

We can see the flag is being stored in a file called ".flag.txt" in the root directory.

Our final step is using the vi text editor as sudo to read the contents of ".flag.txt", which can be done with the command ```sudo vi /root/.flag.txt```.

```picoCTF{uS1ng_v1m_3dit0r_1cee9dcb}```
