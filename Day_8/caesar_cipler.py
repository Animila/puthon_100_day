from caesar_cipler_art import logo

alhabet_eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alhabet_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л',
               'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
               'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
print(logo)

def caesar(text_secret, shift_secret, direction_secret, language):
    secret = ''
    if language == "ru":
        alhabet = alhabet_rus
    elif language == "eng":
        alhabet = alhabet_eng
    for char in text_secret:
        if char in alhabet:
            position = alhabet.index(char)

            if direction_secret == "encode":
                new_position = position + shift_secret
            elif direction_secret == "decode":
                new_position = position - shift_secret
            else:
                return print("Process finished with exit code 0")

            if new_position >= len(alhabet) - 1:
                if language == "eng":
                    new_position -= 26
                elif language == "ru":
                    new_position -= 33
            secret += alhabet[new_position]
        else:
            secret += char
    print(f"Зашифрованный текст: {secret}")

while exit:
    direction = input("Введите 'encode' для шифровки и 'decode' для расшифровки или другое для выхода:\n")
    language = input("Выберите язык (ru/eng): ")
    text = input("Введите текст для зашифровки:\n").lower()
    shift = int(input("Шаг шифровки:\n"))

    if shift >= 45:
        shift = shift % 25

    caesar(text_secret=text, shift_secret=shift, direction_secret=direction, language=language)
    var = input("Напишите 'yes', чтобы продолжить работу или 'no': \n").lower()
    if var == 'yes':
        exit = True
    elif var == 'no':
        print("Спасибо за использование")
        input("Нажмите Enter для закрытия")
        exit = False
    else:
        print("Ошибка")
