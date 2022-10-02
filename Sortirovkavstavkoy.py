def insertion_sort(a):
    
    for i in range(len(a)):
        b = a[i]
        j = i - 1
        
        while ((j >= 0) and (a[j] > b)):
            a[j+1] = a[j]
            j -= 1
       
        a[j+1] = b
    return a
    # Козаренко Д.А., Физ.фак, 4 группа ИВТ 2 курс
