sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# dict_word = sentence.split()
#
# result = {word: len(word) for word in dict_word}
# print(dict_word)
#
# print(result)

result = {word:len(word) for word in sentence.split()}
print(result)