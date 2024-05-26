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
