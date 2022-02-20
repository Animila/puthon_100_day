enemies = 1


def increase_enemies():
    enemies = 2
    print(f'enemies внутри равен: {enemies}')


increase_enemies()
print(f'enemies снаружи равен {enemies}')


player_health = 10

def drink():
    potion = 2
    print(player_health)

drink()
print(player_health)
