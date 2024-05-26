# Transformation

## Description

I wonder what this really is... [enc](https://mercury.picoctf.net/static/77a2b202236aa741e988581e78d277a6/enc "Encoded Text File")

```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

## Hints

* You may find some decoders online

## Walkthrough

THIS WALKTHROUGH IS UNFINISHED

```灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽```

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

```python
plain_text = 'test'
encoded_text = ''
for i in range(0, len(plain_text), 2):
    first_character_in_unicode = ord(plain_text[i])
    second_character_in_unicode = ord(plain_text[i + 1])
    first_character_in_unicode_after_8_bit_shift = first_character_in_unicode << 8
    two_byte_long_new_character_in_unicode = first_character_in_unicode_after_8_bit_shift + second_character_in_unicode
    two_byte_long_new_character = chr(two_byte_long_new_character_in_unicode)
    encoded_text += two_byte_long_new_character
print(encoded_text)
```



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
