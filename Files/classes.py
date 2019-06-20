from random import randint

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

    def count_bomb(self, x, y, n, m, field):
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

def create_bomb(n, m, field):
    x = randint(0, n-1)
    y = randint(0, m-1)
    if field[x][y].bomb == 0:
        field[x][y].be_bomb()
    else:
        create_bomb(n, m, field)

def generate_field(n, m, mines, field):
    for i in range(0,n):
        for j in range(0,m):
            new = box()
            field[i].append(new)

    for i in range(0, mines):
        create_bomb(n, m, field)

def total_count(n, m, field):
    for x in range(0,n):
        for y in range(0,m):
            field[x][y].count_bomb(x, y, n, m, field)
