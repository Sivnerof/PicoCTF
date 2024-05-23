# Python Wrangling

## Description

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](./ende.py "Python program that encrypts or decrypts a file") using [this password](./pw.txt "Password Text File") to get [the flag](./flag.txt.en "Encrypted Flag")?

## Hints

* Get the Python script accessible in your shell by entering the following command in the Terminal prompt: ```$ wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py```

* ```$ man python```

## Walkthrough

This one's fairly simple, all that's required is a basic understanding of how to run a Python program. We're given three files for this challenge; [ende.py](./ende.py "Python program that encrypts or decrypts a file"), [pw.txt](./pw.txt "Password File"), and [flag.txt.en](./flag.txt.en "Encrypted Flag File").

A brief glance at the code within the [ende.py](./ende.py "Python program that encrypts or decrypts a file") file is all we need to understand that this Python program takes a file as input and either encrypts or decrypts it based on whether we supply ```-d``` (decrypt) or ```-e``` (encrypt) as a command line argument.

```python
import sys
import base64
from cryptography.fernet import Fernet



usage_msg = "Usage: "+ sys.argv[0] +" (-e/-d) [file]"
help_msg = usage_msg + "\n" +\
        "Examples:\n" +\
        "  To decrypt a file named 'pole.txt', do: " +\
        "'$ python "+ sys.argv[0] +" -d pole.txt'\n"



if len(sys.argv) < 2 or len(sys.argv) > 4:
    print(usage_msg)
    sys.exit(1)



if sys.argv[1] == "-e":
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3]

    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    c = Fernet(ssb_b64)

    with open(sys.argv[2], "rb") as f:
        data = f.read()
        data_c = c.encrypt(data)
        sys.stdout.write(data_c.decode())


elif sys.argv[1] == "-d":
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3]

    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    c = Fernet(ssb_b64)

    with open(sys.argv[2], "r") as f:
        data = f.read()
        data_c = c.decrypt(data.encode())
        sys.stdout.buffer.write(data_c)


elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(help_msg)
    sys.exit(1)


else:
    print("Unrecognized first argument: "+ sys.argv[1])
    print("Please use '-e', '-d', or '-h'.")

```

We can also skip glancing at the code altogether and just run the program with the ```-h``` (help) command line argument to learn how to use the program.

```$ python3 ende.py -h```

Which results in the following text:

> Usage: ende.py (-e/-d) [file]
> Examples:
>  To decrypt a file named 'pole.txt', do: '$ python ende.py -d pole.txt'

Now that we know how to run this program we can use the following command to decrypt the flag in [flag.txt.en](./flag.txt.en "Encrypted Flag"):

```python3 ende.py -d flag.txt.en```

Once prompted by the program to input the password, we'll use the one given to us in the [pw.txt](./pw.txt "Password File") file.

```192ee2db192ee2db192ee2db192ee2db```

After inputing the correct password the flag will be printed to the terminal.

```
$ python3 ende.py -d flag.txt.en

Please enter the password:192ee2db192ee2db192ee2db192ee2db
picoCTF{4p0110_1n_7h3_h0us3_192ee2db}
```

Encrypted: ```gAAAAABgUAIVX7N_dNxY0j5lWtsDEN2b-h0mN-Lyhm_9QaEdwFK4em1kGiAV52ewbKv8wZJL2QwecZ7kTsVQ11PYEL3BJLD4LVyKrCKAvTFu5-1yuNGFAXKBY8GO3nIReXuOUbaSwVHl```

Decrypted with ```192ee2db192ee2db192ee2db192ee2db``` as password:
```picoCTF{4p0110_1n_7h3_h0us3_192ee2db}```
