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
print(encoded_text)
```













---

```python
encoded_flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽'
decoded_flag = ''.join([chr((ord(c) >> 8) & 0xFF) + chr(ord(c) & 0xFF) for c in encoded_flag])
print(decoded_flag)
```

```picoCTF{16_bits_inst34d_of_8_75d4898b}```

p = 112
i = 105

p = 112 or 1110000 (64, 32, 16 = 112)
p after bit shift = 1110000 00000000 (28672)

28672 + 105 = 28777

```
>>> ord("灩")
28777
```

28777 (111000001101001) >> 8 =  000000001110000 (112)

```
$ python3
>>> ord("p")
112
>>> ord("i")
105

```

28777 (111000001101001) >> 8 =  000000001110000 (112)
28777 (111000001101001) & 0xFF = 

255 =  11111111

(ord(c) >> 8) & 0xFF)
000000001110000 (112)
000000011111111 (255)
---------------------
000000001110000 (112)


chr(ord(c) & 0xFF)
111000001101001 (28777)
000000011111111 (255)
---------------
000000001101001 (105)



```
Before: 111000001101001

(ord(c) >> 8) & 0xFF)
000000001110000 (112)
000000011111111 (255)
---------------------
000000001110000 (112)


chr(ord(c) & 0xFF)
111000001101001 (28777)
000000011111111 (255)
---------------
000000001101001 (105)
```


```python
encoded_flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽'
decoded_flag = ''
for c in encoded_flag:
  character_in_unicode = ord(c)
  #push greatest byte into lowest byte
  character_in_unicode_after_8_bit_shift = character_in_unicode >> 8
  character_in_unicode_after_8_bit_shift_bitwise_and = character_in_unicode_after_8_bit_shift & 0xFF
  character_in_unicode_bitwise_and = character_in_unicode & 0xFF
  decoded_character_1 = chr(character_in_unicode_after_8_bit_shift_bitwise_and)
  decoded_character_2 = chr(character_in_unicode_bitwise_and)
  decoded_flag += decoded_character_1
  decoded_flag += decoded_character_2
print(decoded_flag)

decoded_flag = ''.join([chr((ord(c) >> 8) & 0xFF) + chr(ord(c) & 0xFF) for c in encoded_flag])
print(decoded_flag)
```
