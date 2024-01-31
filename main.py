def cipher_decoding(memory,step):
    plain_text = ""
    for c in memory:
        c_unicode = ord(c)
        c_index = ord(c) - ord("а")
        new_index = (c_index - step) % 33
        new_unicode = new_index + ord("а")
        new_character = chr(new_unicode)
        plain_text = plain_text + new_character
    return plain_text