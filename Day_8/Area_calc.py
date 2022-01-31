import math


def paint_calc(height, width, cover):
    need = math.ceil((height * width) / cover)
    print(f"Нужно {need} банки красок")


test_h = int(input("Высота стены: "))
test_w = int(input("Длина стены: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
