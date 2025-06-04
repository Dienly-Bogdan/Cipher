import sys

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    GREEN = Fore.GREEN
    RED = Fore.RED
    RESET = Style.RESET_ALL
except ImportError:
    GREEN = RED = RESET = ""

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('А') if char.upper() == char and 'А' <= char <= 'Я' else \
                   ord('а') if char.islower() and 'а' <= char <= 'я' else \
                   ord('A') if char.isupper() and 'A' <= char <= 'Z' else \
                   ord('a') if char.islower() and 'a' <= char <= 'z' else 0
            if base:
                offset = 32 if 'А' <= char <= 'Я' or 'а' <= char <= 'я' else 26
                result += chr((ord(char) - base + shift) % offset + base)
            else:
                result += char
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0
    for char in text:
        if char.isalpha():
            k = ord(key[key_index % key_length]) - ord('a')
            if char.isupper():
                base = ord('A')
                result += chr((ord(char) - base + k) % 26 + base)
            elif char.islower():
                base = ord('a')
                result += chr((ord(char) - base + k) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0
    for char in text:
        if char.isalpha():
            k = ord(key[key_index % key_length]) - ord('a')
            if char.isupper():
                base = ord('A')
                result += chr((ord(char) - base - k + 26) % 26 + base)
            elif char.islower():
                base = ord('a')
                result += chr((ord(char) - base - k + 26) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def main():
    print(f"{GREEN}Добро пожаловать в программу шифрования!{RESET}")
    while True:
        try:
            print("\nВыберите действие:\n1. Зашифровать текст\n2. Расшифровать текст\n3. Выход")
            action = input("Выбор: ").strip()
            if action == "3":
                print("Выход.")
                break
            if action not in ["1", "2"]:
                print(f"{RED}Неверный ввод. Попробуйте снова.{RESET}")
                continue

            text = input("Введите текст: ")
            print("\nВыберите алгоритм:\n1. Цезарь\n2. Виженер")
            algo = input("Выбор: ").strip()
            if algo == "1":
                try:
                    shift = int(input("Введите сдвиг: "))
                except ValueError:
                    print(f"{RED}Сдвиг должен быть числом!{RESET}")
                    continue
                if action == "1":
                    result = caesar_encrypt(text, shift)
                else:
                    result = caesar_decrypt(text, shift)
            elif algo == "2":
                key = input("Введите ключевое слово (только латиница): ").strip()
                if not key.isalpha():
                    print(f"{RED}Ключ должен содержать только буквы!{RESET}")
                    continue
                if action == "1":
                    result = vigenere_encrypt(text, key)
                else:
                    result = vigenere_decrypt(text, key)
            else:
                print(f"{RED}Неверный выбор алгоритма!{RESET}")
                continue

            print(f"{GREEN}Результат: {result}{RESET}")
        except KeyboardInterrupt:
            print("\nВыход.")
            break

if __name__ == "__main__":
    main()