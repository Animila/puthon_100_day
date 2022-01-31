total = 0
for two_number in range(2, 101, 2):
    total += two_number
print(total)

total2 = 0
for two_number in range(1, 101):
    if two_number % 2 == 0:
        total2 += two_number
print(total2)