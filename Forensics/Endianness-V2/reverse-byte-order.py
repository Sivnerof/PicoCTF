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
