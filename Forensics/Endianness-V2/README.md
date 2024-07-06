# Endianness V2

## Description

Here's a file that was recovered from a 32-bits system that organized the bytes a weird way. We're not even sure what type of file it is. Download it [here](https://artifacts.picoctf.net/c_titan/112/challengefile "Pico CTF link to download challenge file") and see what you can get out of it.

## Hints

* (None)

## Walkthrough

Unfinished Walkthrough

```python
chunk_size = 4

f = open("challengefile", mode="rb")
f2 = open("challengefilereversed", mode="wb")

while True:
    chunk = f.read(chunk_size)
    if not chunk:
        break
    bytes_reversed = chunk[::-1]
    f2.write(bytes_reversed)

f.close()
f2.close()
```


