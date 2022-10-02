def drawSymbolPlot(func, a, b, c):

    oll_x = [a + string*((b - a) / (c)) for string in range(c+1) ]
    oll_y= [int(func(x)) for x in oll_x]

    left_edge = min(oll_y)
    for y in oll_y:
        pos = y - left_edge
        print(' ' * pos + '*')
        print ()
    
    print()
    print()
    # Козаренко Д.А., Физ.фак, 4 группа ИВТ 2 курс