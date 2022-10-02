def bubble_sort(a):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                not_sorted = True
    return a
# Козаренко Д.А., Физ.фак, 4 группа ИВТ 2 курс


