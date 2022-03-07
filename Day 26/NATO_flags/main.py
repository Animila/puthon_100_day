import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alhabet = data.to_dict()
nato_alhabet = {row.letter:row.code for (index, row) in data.iterrows()}
# {new_key:new_value for (index, row) in df.iterrows()}
print(nato_alhabet)

word = input("Ваше слово: ").upper()
output_list = [nato_alhabet[letter] for letter in word]

output_word = ''
for i in output_list:
    output_word += i
    output_word += "\n"

print(output_word)