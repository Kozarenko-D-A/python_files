def binary_search(a, b):   # a- значение, b- массив
    left = 0
    right = len(b)
    while left <= right:
        mid = (left + right) // 2
        if b[mid] == a:
            return mid
        if a > b[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Козаренко Д.А., Физ.фак, 4 группа ИВТ 2 курс