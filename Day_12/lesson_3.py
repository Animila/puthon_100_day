enemies = 1


def increase_enemies():
    global enemies  # модифицировать
    enemies += 1
    print(f'enemies внутри равен {enemies}')
    return enemies + 1  # без модификации


increase_enemies()
print(f'enemies снаружи равен {enemies}')
