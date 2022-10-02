from random import random


def monte_carlo_integration(func, a, b, h):  # a-это нижний край, b- верхнтй край, h- количество точек
    y_min = float('inf')
    y_max = float('-inf')
    i = a
    while i <= b:
        f = func(i)
        y_min = min(y_min, f)
        y_max = max(y_max, f)
        i += 1
    c = 0
    for i in range(h):
        x = a + random() * (b - a)
        f = y_min + random() * (y_max - y_min)
        if f <= y_min + func(x):
            c += 1
    return (b - a) * (y_max - y_min) * c / h

# Козаренко Д.А., Физ.фак, 4 группа ИВТ 2 курс

