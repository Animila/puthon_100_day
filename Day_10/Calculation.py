def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mult(n1, n2):
    return n1*n2

def dev(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": dev,
}
def calculation():
    exit = False
    number_1 = float(input("Какое первое число?: "))

    while not exit:
        number_2 = float(input("Какое следующее число?: "))

        for symbols in operation:
            print(symbols)
        function = input("Выберите функцию:")

        answer = operation[function](number_1, number_2)
        print(f"{number_1} {function} {number_2} = {answer}")

        if input(f"Напишите 'y' если продолжить работу с {answer}, или напишите 'n' чтобы выйти: ") == "y":
            number_1 = answer
            exit = False
        else:
            exit = True
            calculation()

calculation()