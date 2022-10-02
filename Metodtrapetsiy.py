def trapeze_integration(func, a, b, c):
    dx = (b - a) / c
    s = 0
    for i in range(c - 1):
        x = a + dx * i
        s += (dx*(func((x + dx)) + func(x)) / 2)
    return s


def func(x):
    return x*x
    # Козаренко Д.А., Физ.фак, 4 группа ИВТ 2 курс