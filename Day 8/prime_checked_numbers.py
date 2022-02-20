def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Простое число")
    else:
        print("Не простое число")



n = int(input("Проверить число: "))
prime_checker(number=n)