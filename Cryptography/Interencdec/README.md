# Interencdec

## Description

Can you get the real meaning from this file. Download the file [here](https://artifacts.picoctf.net/c_titan/109/enc_flag "Encoded Flag File").

## HInts

* Engaging in various decoding processes is of utmost importance

## Walkthrough

If we open the [enc_flag file](./enc_flag "Encoded flag file") we'll find the following Base 64 encoded text.

```YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyMHdNakV5TnpVNGZRPT0nCg==```

[Base-64](https://en.wikipedia.org/wiki/Base64 "Wikipedia article on Base-64") is a common encoding scheme that converts binary data into a string of printable characters. Every digit in Base-64 has 64 possibilities from lowercase "a" to lowercase "z", uppercase "A" to uppercase "Z", the numbers 0 through 9, and the "+" and "/" characters. The equals sign, "=", is used for padding the string. A common sign that a string is encoded in Base-64 are the double equal signs but this is not always the case. Sometimes a string doesn't need padding and there will be no equal signs. Another good way of telling a string is encoded in Base-64 is that it only makes use of the characters described above. There are many tools online and on your computer that can help in decoding. One such tool is [CyberChef](https://cyberchef.org/ "CyberChef online tool").

After decoding from Base-64 we should see another Base-64 encoded string. This time it is wrapped in single quotes and prefixed with the letter "b", this is how a byte string is declared in Python. We can forget about that and just remove the Base-64 string to decode it again.

```b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX20wMjEyNzU4fQ=='```

```d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX20wMjEyNzU4fQ==```

After decoding the Base-64 string we should get what seems like random gibberish text in the flag format.

```wpjvJAM{jhlzhy_k3jy9wa3k_m0212758}```

Taking this enciphered flag and using a tool like [CyberChef](https://cyberchef.org/#recipe=ROT13_Brute_Force(true,true,false,100,0,true,'')&input=d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX20wMjEyNzU4fQ "CyberChef online tool") to brute force all 25 Caesar shift combinations we'll see that this was enciphered using a shift key of 19.

ROT-19: ```picoCTF{caesar_d3cr9pt3d_f0212758}```
