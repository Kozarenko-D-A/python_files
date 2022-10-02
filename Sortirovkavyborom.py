def selection_sort(b):
    for i in range(len(b)):
        min = b[i]
        minId = i
        for j in range(i+1, len(b)):
            if b[j] < min:
                min = b[j]
                minId = j
        b[minId] = b[i]
        b[i] = min
    return b

# Козаренко Д.А., Физ.фак, 4 группа ИВТ 2 курс

