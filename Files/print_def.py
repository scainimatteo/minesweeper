from __future__ import print_function

def print_value(n, m, field):
    print("------------")
    for i in range(0,n):
        for j in range(0,m):
            print(field[i][j].value, ' ', end = '')
        print('')

def print_bomb(n, m, field):
    for i in range(0,n):
        for j in range(0,m):
            print(field[i][j].bomb, ' ', end = '')
        print('')
