from __future__ import print_function

def print_value(dif, n, m, field):
    print("------------")
    if dif == 1:
        print("     [01][02][03][04][05][06][07][08][09]")
    elif dif == 2:
        print("     [01][02][03][04][05][06][07][08][09][10][11][12][13][14][15][16]")
    elif dif == 3:
        print("     [01][02][03][04][05][06][07][08][09][10][11][12][13][14][15][16][17][18][19][20][21][22][23][24][25][26][27][28][29][30]")


    for i in range(0,n):
        if i < 9:
            print('[0', end = '')
            print((i + 1), end = '')
            print('] ', end = '')
        else:
            print('[', end = '')
            print((i + 1), end = '')
            print('] ', end = '')
            

        for j in range(0,m):
            print(field[i][j].value, '  ', end = '')
        print('')

def print_bomb(n, m, field):
    for i in range(0,n):
        for j in range(0,m):
            print(field[i][j].bomb, ' ', end = '')
        print('')
