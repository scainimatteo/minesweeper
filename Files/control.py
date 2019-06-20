def matrice_next(n, m, field, next_matrix):
    for i in range(0,n):
        for j in range(0,m):
            if field[i][j].bomb == 0:
                next_matrix[i].append(field[i][j].next)
            else:
                next_matrix[i].append("!")

def controllo(n, m, mines, field, next_matrix):
    num = 0
    for i in range(0, n):
        for j in range(0, m):
            if field[i][j].bomb != 1:
                if field[i][j].value == next_matrix[i][j]:
                    num += 1
                else:
                    break
    if num == (n*m - mines):
        return 1
