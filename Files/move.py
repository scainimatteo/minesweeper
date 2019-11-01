def move(n, m, field):
    ctrl = 1
    xmove = int(input("X: "))
    ymove = int(input("Y: "))
    flag = input("Mod: ")
    field[xmove-1][ymove-1].change_value(flag)
    if field[xmove-1][ymove-1].next == 0 and flag != 'f':
        change_0_box((xmove-1), (ymove-1), n, m, field)

    while ctrl != 0:
        ctrl = 0
        for i in range(0, n):
            for j in range(0, m):
                if field[i][j].value == 0 and field[i][j].while_def == 0:
                    ctrl = 1
                    field[i][j].change_while()
                    change_0_box(i, j, n, m, field)

    reset_all_while(n, m, field) 
    return (xmove, ymove)

def change_0_box(x, y, n, m, field):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x == 0:
                if y == 0:
                    for i in range(0, 2):
                        for j in range(0, 2):
                            field[x+i][j+y].change_value(None)

                elif y == (m-1):
                    for i in range(0, 2):
                        for j in range(-1, 1):
                            field[x+i][j+y].change_value(None)

                else:
                    for i in range(0, 2):
                        for j in range(-1, 2):
                            field[x+i][j+y].change_value(None)

            elif x == (n-1):
                if y == 0:
                    for i in range(-1, 1):
                        for j in range(0, 2):
                            field[x+i][j+y].change_value(None)

                elif y == (m-1):
                    for i in range(-1, 1):
                        for j in range(-1, 1):
                            field[x+i][j+y].change_value(None)

                else:
                    for i in range(-1, 1):
                        for j in range(-1, 2):
                            field[x+i][y+j].change_value(None)

            elif y == 0 and x != 0 and x != (n-1):
                for i in range(-1, 2):
                    for j in range(0, 2):
                        field[x+i][j+y].change_value(None)

            elif y == (m-1) and x != 0 and x != (n-1):
                for i in range(-1, 2):
                    for j in range(-1, 1):
                        field[x+i][j+y].change_value(None)

            else:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        field[x+i][j+y].change_value(None)

def reset_all_while(n, m, field):
    for i in range(0,n):
        for j in range(0,m):
            field[i][j].reset_while()

def first_move(n, m, field, x, y):
    ctrl = 1
    flag = '0'
    field[x-1][y-1].change_value(flag)
    if field[x-1][y-1].next == 0 and flag != 'f':
        change_0_box((x-1), (y-1), n, m, field)

    while ctrl != 0:
        ctrl = 0
        for i in range(0, n):
            for j in range(0, m):
                if field[i][j].value == 0 and field[i][j].while_def == 0:
                    ctrl = 1
                    field[i][j].change_while()
                    change_0_box(i, j, n, m, field)

    reset_all_while(n, m, field) 
