def rectangle_integration(func, a, b, c):
    dx = (b - a) / c
    s = 0
    for i in range(c):
        x = a + dx * i
        s += dx * func(x)
    return s
# Козаренко Д.А., Физ.фак, 4 группа ИВТ 2 курс