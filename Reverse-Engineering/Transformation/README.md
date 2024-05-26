# Transformation

## Description

I wonder what this really is... [enc](https://mercury.picoctf.net/static/77a2b202236aa741e988581e78d277a6/enc "Encoded Text File")

```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

## Hints

* You may find some decoders online

## Walkthrough

For this challenge we're given a text file named [enc](./enc "Text file with encoded text") which contains encoded text. At first glance the text appears to be Chinese, but putting the characters into a translator just returns gibberish.

```灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽```

We're also given the following Python code.

```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

At first, the code seems pretty intimidating but studying the code and rewriting it makes it a little easier to understand.

```python
plain_text = 'test'
encoded_text = ''

# The loop will skip every other character because it operates on two characters at a time.
for i in range(0, len(plain_text), 2):

    # Get current characters unicode value
    current_char_unicode = ord(plain_text[i])

    # Get next characters unicode value
    next_char_unicode = ord(plain_text[i + 1])

    # The current character value will bit shift 8 positions to the left
    # Example: Lowercase t (decimal: 116) goes from 01110100 to 0111010000000000 (decimal: 29696)
    current_char_unicode_8_bit_shift = current_char_unicode << 8

    # Add the 8-bit shifted current character value and the next characters unicode value
    new_unicode = current_char_unicode_8_bit_shift + next_char_unicode

    # Get the character at the new unicode location
    new_character = chr(new_unicode)

    # Add the new character to the encoded text
    encoded_text += new_character

# The word 'test' encodes to 瑥獴
print(encoded_text)
```

Breakdown of the program:
* The python program operates on two characters at a time.
* The current characters unicode value in every loop is made larger by 8 bits (one byte).
  * Example: Lowercase t (decimal: 116) goes from 01110100 to 0111010000000000 (decimal: 29696)
* This results in a much larger number with 8 trailing zeroes.
* Those 8 trailing zeroes are then used as storage for the next characters unicode value. This is done by adding the two values together.
* This new value is interesting because it contains in the higher byte the current characters unicode value, and in the lower byte it contains the next characters unicode value.
* The character representation of the new unicode value is then added to the string and the loop repeats, encoding all two letter pairs into a single character.

Essentially this means that every character in the encoded text is made up of 16 bits (2 bytes), where the upper byte represents one character on the ASCII chart and the lower byte represents another.

Below is a table that shows how the output from the program above ("瑥獴") relates to the plaintext word "test". The table can also be used to give you an idea of how to manually decode the encoded text given in this CTF.

|                          |                  |                  |
|:------------------------:|:----------------:|:----------------:|
| **CHARACTER**            | 瑥                | 獴                |
| **DECIMAL**              | 29797            | 29556            |
| **BINARY**               | 0111010001100101 | 0111001101110100 |
| **UPPER BYTE**           | 01110100         | 01110011         |
| **LOWER BYTE**           | 01100101         | 01110100         |
| **UPPER BYTE DECIMAL**   | 116              | 115              |
| **LOWER BYTE DECIMAL**   | 101              | 116              |
| **UPPER BYTE CHARACTER** | t                | s                |
| **LOWER BYTE CHARACTER** | e                | t                |
| **CHARACTERS TOGETHER**  | te               | st               |


Now that we know the encoding process, we can write a Python program to decode the characters given.

```python
encoded_flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽'
decoded_flag = ''

for char in encoded_flag:

  # Get the characters unicode value
  character_unicode = ord(char)

  # Convert the unicode to binary (zero-padded 16 bits)
  character_in_binary = format(character_unicode, '016b')

  # Grab the higher byte (left 8 bits)
  higher_byte = character_in_binary[:8]

  # Grab the lower byte (right 8 bits)
  lower_byte = character_in_binary[8:]

  # Convert the higher byte to decimal
  higher_byte_in_decimal = int(higher_byte, 2)

  # Convert the lower byte to decimal
  lower_byte_in_decimal = int(lower_byte, 2)
  
  # Convert the higher byte in decimal to ASCII
  first_character = chr(higher_byte_in_decimal)

  # Convert the lower byte in decimal to ASCII
  second_character = chr(lower_byte_in_decimal)

  # Append the first decoded character to the decoded flag
  decoded_flag += first_character

  # # Append the second decoded character to the decoded flag
  decoded_flag += second_character
print(decoded_flag)
```

After running the above program we should get the following flag.

```picoCTF{16_bits_inst34d_of_8_75d4898b}```
