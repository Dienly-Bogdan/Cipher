# Задача Расшифровать и Зашрифовать/ Строки и Число. 
# Функция Расшифровки Числа
def decipher_number(memory, step):
    return memory - step

def cipher_line(memory,step):
    new_word = ""
    for letter in memory:
        lst = list(range(1072,1103))
        if ord(letter) in lst:
            code = ord(letter) + step
            new_word += chr(code)
    return new_word

def decipher_line(memory,step):
    plain_text = ""
    for c in memory:
        c_unicode = ord(c)
        c_index = ord(c) - ord("а")
        new_index = (c_index - step) % 33
        new_unicode = new_index + ord("а")
        new_character = chr(new_unicode)
        plain_text = plain_text + new_character
    return plain_text

def cipher_number(memory, step):
    return memory + step