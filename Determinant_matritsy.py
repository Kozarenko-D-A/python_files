def determinant(m):
    det = 0
    if len(m) == 1:
        return m[0]
    if len(m) == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    else:
        sgn = 1
        for nm_index in range(len(m[0])):
            sub_matrix = [[*line[:nm_index], *line[nm_index+1:]] for line in m[1:]]
            det += sgn * m[0][nm_index] * determinant(sub_matrix)
            sgn *= -1
    return det
    # Козаренко Д.А., Физ.фак, 4 группа ИВТ 2 курс