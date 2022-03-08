# def add(*args):
#     arg_list = []
#     for n in args:
#         arg_list.append(n)
#     print(arg_list[2])
#
#
# add(3, 4, 5, 6)

def add(*numbers):
    print(numbers[0])
    print(numbers)
    print(type(numbers))
    count = 0
    for n in numbers:
        count += n
    return count


print(add(5, 5, 5))
