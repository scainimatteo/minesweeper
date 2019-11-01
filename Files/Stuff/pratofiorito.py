from __future__ import print_function
from random import *

print("Modalita disponibili:\n[1] facile (9*9, 10)\n[2] media (16*16, 40)\n[3] difficile (16*30, 99)")
mod = int(input("Modalita: "))
if mod == 1:
    n = 9
    m = 9
    mines = 10

elif mod == 2:
    n = 16
    m = 16
    mines = 40

elif mod == 3:
    n = 16
    m = 30
    mines = 99

field = [[] for i in range(0,n)]
next_matrix = [[] for i in range(0, n)]

class box():
    def __init__(self):
        self.value = '*'
        self.bomb = 0
        self.next = 0
        self.while_def = 0

    def be_bomb(self):
        self.bomb = 1

    def change_value(self, flag):
        if flag == 'f':
            if self.value == '*':
                self.value = '+'
            elif self.value == '+':
                self.value = '*'
        else:
            if self.bomb == 1:
                self.value = '!'
                self.next = -1
            else:
                self.value = self.next

    def change_while(self):
        self.while_def = 1

    def reset_while(self):
        self.while_def = 0

    def count_bomb(self, x, y):
        if self.bomb == 0:
            if x == 0:
                if y == 0:
                    for i in range(0, 2):
                        for j in range(0, 2):
                            if field[x+i][y+j].bomb == 1:
                                self.next += 1

                elif y == (m-1):
                    for i in range(0, 2):
                        for j in range(-1, 1):
                            if field[x+i][y+j].bomb == 1:
                                self.next += 1

                else:
                    for i in range(0, 2):
                        for j in range(-1, 2):
                            if field[x+i][y+j].bomb == 1:
                                self.next += 1

            elif x == (n-1):
                if y == 0:
                    for i in range(-1, 1):
                        for j in range(0, 2):
                            if field[x+i][y+j].bomb == 1:
                                self.next += 1

                elif y == (m-1):
                    for i in range(-1, 1):
                        for j in range(-1, 1):
                            if field[x+i][y+j].bomb == 1:
                                self.next += 1

                else:
                    for i in range(-1, 1):
                        for j in range(-1, 2):
                            if field[x+i][y+j].bomb == 1:
                                self.next += 1

            elif y == 0 and x != 0 and x != (n-1):
                for i in range(-1, 2):
                    for j in range(0, 2):
                        if field[x+i][y+j].bomb == 1:
                            self.next += 1

            elif y == (m-1) and x != 0 and x != (n-1):
                for i in range(-1, 2):
                    for j in range(-1, 1):
                        if field[x+i][y+j].bomb == 1:
                            self.next += 1

            else:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if field[x+i][y+j].bomb == 1:
                            self.next += 1

def create_bomb():
    x = randint(0, n-1)
    y = randint(0, m-1)
    if field[x][y].bomb == 0:
        field[x][y].be_bomb()
    else:
        create_bomb()

def generate_field():
    for i in range(0,n):
        for j in range(0,m):
            new = box()
            field[i].append(new)

    for i in range(0, mines):
        create_bomb()

def total_count():
    for x in range(0,n):
        for y in range(0,m):
            field[x][y].count_bomb(x, y)

def move():
    ctrl = 1
    xmove = int(input("X: "))
    ymove = int(input("Y: "))
    flag = input("Mod: ")
    field[xmove-1][ymove-1].change_value(flag)
    if field[xmove-1][ymove-1].next == 0 and flag != 'f':
        change_0_box((xmove-1), (ymove-1))

    while ctrl != 0:
        ctrl = 0
        for i in range(0, n):
            for j in range(0, m):
                if field[i][j].value == 0 and field[i][j].while_def == 0:
                    ctrl = 1
                    field[i][j].change_while()
                    change_0_box(i, j)

    reset_all_while() 
    return (xmove, ymove)

def change_0_box(x, y):
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

def reset_all_while():
    for i in range(0,n):
        for j in range(0,m):
            field[i][j].reset_while()

def print_value():
    print("------------")
    for i in range(0,n):
        for j in range(0,m):
            print(field[i][j].value, ' ', end = '')
        print('')

def print_bomb():
    for i in range(0,n):
        for j in range(0,m):
            print(field[i][j].bomb, ' ', end = '')
        print('')

def matrice_next():
    for i in range(0,n):
        for j in range(0,m):
            if field[i][j].bomb == 0:
                next_matrix[i].append(field[i][j].next)
            else:
                next_matrix[i].append("!")

def controllo():
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
        
generate_field()
total_count()
print_bomb()
matrice_next()
while 1:
    try:
        print_value()
        x, y = move()
        win = controllo()
        if field[x - 1][y - 1].value == '!':
            print("HAI PERSO")
            break
        if win == 1:
            print("HAI VINTO!")
            break
    except KeyboardInterrupt:
        break
