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
