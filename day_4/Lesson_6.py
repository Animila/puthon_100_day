row_1 = ["-", "-", "-"]
row_2 = ["-", "-", "-"]
row_3 = ["-", "-", "-"]

map = [row_1, row_2, row_3]

print(f"{row_1}\n{row_2}\n{row_3}")

position = input("В какой квадрат выхотите попасть?\n")

x_position = int(position) // 10 - 1
y_position = int(position) % 10 - 1

map[y_position][x_position] = "x"

print(f"{row_1}\n{row_2}\n{row_3}")