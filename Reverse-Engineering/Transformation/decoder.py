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
