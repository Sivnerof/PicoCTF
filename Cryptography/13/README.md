# 13

## Description

Cryptography can be easy, do you know what ROT13 is? ```cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}```

## Hints

* This can be solved online if you don't want to do it by hand!

## Walkthrough

[ROT-13](https://en.wikipedia.org/wiki/ROT13 "ROT-13 Wikipedia Article"), short for "rotate by 13", refers to a type of shift cipher where letters are enciphered by adding 13 to their numeric value, with a mod of 26. For example, if A is equal to 0 then A becomes N when 13 is added. When 13 is added to N then the result is A, because of mod 26 we end up wrapping back around to 0. This means that encryption and decryption for ROT-13 is exactly the same, just add 13.

|   |     |     |   |
|:---:|:---:|:---:|:---:|
| A | --> | <-- | N |
| B | --> | <-- | O |
| C | --> | <-- | P |
| D | --> | <-- | Q |
| E | --> | <-- | R |
| F | --> | <-- | S |
| G | --> | <-- | T |
| H | --> | <-- | U |
| I | --> | <-- | V |
| J | --> | <-- | W |
| K | --> | <-- | X |
| L | --> | <-- | Y |
| M | --> | <-- | Z |

Deciphering ROT-13 is very easy, it can be done manually using the table above, or you can use one of the many online tools that specialize in ROT-13.

Below is a Python program to decipher the flag.

```python
enciphered_flag = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
deciphered_flag = ''

# 65
ascii_uppercase_a = ord('A')

# 97
ascii_lowercase_a = ord('a')

def rot13(ascii_base_value):
    # Subtract the ASCII base value to get the alphabet position (0-25)
    alphabet_position = ord(char) - ascii_base_value

    # Rotate 13 positions with mod 26
    rot_13 = (alphabet_position + 13) % 26

    # Add the ASCII base value back to get the new ASCII position
    ascii_position = rot_13 + ascii_base_value

    # Get the character at the new ascii position
    deciphered_char = chr(ascii_position)

    # Return the newly deciphered character
    return deciphered_char

for char in enciphered_flag:

    # Uppercase English letters
    if char >= 'A' and char <= 'Z':
        deciphered_flag += rot13(ascii_uppercase_a)

    # Lowercase English letters
    elif char >= 'a' and char <= 'z':
        deciphered_flag += rot13(ascii_lowercase_a)

    # Append symbols, non-English characters, numbers, etc.
    else:
        deciphered_flag += char
print(deciphered_flag)
```

```picoCTF{not_too_bad_of_a_problem}```
