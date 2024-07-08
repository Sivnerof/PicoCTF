# Grab chunks in 4 byte sizes
chunk_size = 4

# Open challengefile in read bytes mode
f1 = open("challengefile", mode="rb")

# Open challengefilereversed in write bytes mode
f2 = open("challengefilereversed", mode="wb")

# Repeat until there are no chunks being read
while True:

    # Read chunk_size byes from file and store them in chunk variable
    chunk = f1.read(chunk_size)

    # No more chunks, end loop
    if not chunk:
        break

    # Reverse bytes and store them in bytes_reversed
    bytes_reversed = chunk[::-1]

    # Write reversed bytes to challengefilereversed file
    f2.write(bytes_reversed)

# Close open file handles
f1.close()
f2.close()
