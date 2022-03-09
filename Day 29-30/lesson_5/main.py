import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    word = input("Введите слово: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Данных символов нет в алфавите")
    else:
        print(output_list)

# Можно было все обернуть в функцию и вызвать снаружи
