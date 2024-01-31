# Задача Расшифровать и Зашрифовать/ Строки и Возраст.

def cipher_line(memory,step):
    new_word = ""
    for letter in memory:
        lst = list(range(1072,1103))
        if ord(letter) in lst:
            code = ord(letter) + step
            new_word += chr(code)
    return new_word


