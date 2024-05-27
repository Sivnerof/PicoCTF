enciphered_flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"
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
