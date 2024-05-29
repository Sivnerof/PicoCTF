# Caesar

## Description

Decrypt this [message](https://jupiter.challenges.picoctf.org/static/6385b895dcb30c74dbd1f0ea271e3563/ciphertext "Enciphered flag file").

## Hints

* caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher "Caesar Cipher tutorial")

## Walkthrough

A [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher "Caesar Cipher Wikipedia Article") is a simple type of substitution cipher where each letter in the plaintext is shifted x amount of times.

The formula for encrypting a single character using a Caesar Cipher is as follows.

```E = (n + k) mod 26```

Here "E" represents the enciphered character, and "n" represents the number of the character needing to be enciphered and "k" represents the key (shift amount).

For example to encrypt the letter "A" with a shift of 3 we would do the following (assume A=0).

```(0 + 3) mod 26 = 3```

The character at position 3 would be "D" (A=0, B=1, C=2, D=3).

The formula for decryption of a single character is similar except we subtract the key from the enciphered characters number.

```D = (n - k) mod 26```

For example, to decipher the letter "D" we enciphered during the above steps, we would do the following.

```(3 - 3) mod 26 = 0```

Giving us the character at position 0, the letter "A".

When the key is not known, a brute force of all possible keys can be attempted with relative ease since their are only 26 different possibilities, assuming the cipher used the English alphabet.

One tool that we can use for this brute force solution is [CyberChef](https://cyberchef.org/#recipe=ROT13_Brute_Force(true,true,false,100,0,true,'')&input=ZHNwdHRqb2h1aWZzdmNqZHBvYWJya3R0ZHM "CyberChef ROT Brute Force") which will print the output below.

```
Amount =  1: etquukpivjgtwdkeqpbcsluuet
Amount =  2: furvvlqjwkhuxelfrqcdtmvvfu
Amount =  3: gvswwmrkxlivyfmgsrdeunwwgv
Amount =  4: hwtxxnslymjwzgnhtsefvoxxhw
Amount =  5: ixuyyotmznkxahoiutfgwpyyix
Amount =  6: jyvzzpunaolybipjvughxqzzjy
Amount =  7: kzwaaqvobpmzcjqkwvhiyraakz
Amount =  8: laxbbrwpcqnadkrlxwijzsbbla
Amount =  9: mbyccsxqdrobelsmyxjkatccmb
Amount = 10: nczddtyrespcfmtnzyklbuddnc
Amount = 11: odaeeuzsftqdgnuoazlmcveeod
Amount = 12: pebffvatgurehovpbamndwffpe
Amount = 13: qfcggwbuhvsfipwqcbnoexggqf
Amount = 14: rgdhhxcviwtgjqxrdcopfyhhrg
Amount = 15: sheiiydwjxuhkrysedpqgziish
Amount = 16: tifjjzexkyvilsztfeqrhajjti
Amount = 17: ujgkkafylzwjmtaugfrsibkkuj
Amount = 18: vkhllbgzmaxknubvhgstjcllvk
Amount = 19: wlimmchanbylovcwihtukdmmwl
Amount = 20: xmjnndiboczmpwdxjiuvlennxm
Amount = 21: ynkooejcpdanqxeykjvwmfooyn
Amount = 22: zolppfkdqeboryfzlkwxngppzo
Amount = 23: apmqqglerfcpszgamlxyohqqap
Amount = 24: bqnrrhmfsgdqtahbnmyzpirrbq
Amount = 25: crossingtherubiconzaqjsscr
```

Looking at the output produced by a shift of 25 we'll see the text "```crossingtherubiconzaqjsscr```", a reference to Julius Caesar's infamous [crossing of the Rubicon](https://en.wikipedia.org/wiki/Crossing_the_Rubicon "Wikipedia article on Caesar's crossing of the Rubicon").

Enciphered Flag: ```picoCTF{dspttjohuifsvcjdpoabrkttds}```

Deciphered Flag: ```picoCTF{crossingtherubiconzaqjsscr}```
