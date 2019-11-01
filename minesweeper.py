from __future__ import print_function
from random import randint
from Files import print_def 
from Files import classes
from Files import control
from Files import move
import sys

sys.path.insert(0, '~/Desktop/Matteo/Informatica/Python/PratoFiorito/Files')
print("Modalita disponibili:\n[1] facile (9*9, 10)\n[2] media (16*16, 40)\n[3] difficile (16*30, 99)")
try:
    mod = int(input("Modalita: "))
except:
    print("Interruzione")
    sys.exit()
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

classes.generate_field(n, m, mines, field)
# classes.total_count(n, m, field)
control.matrice_next(n, m, field, next_matrix)
print("0 per uscire")
while 1:
    try:
        print_def.print_value(mod, n, m, field)
        while 1:
            try:
                x, y = move.move(n, m, field)
                break
            except:
                print("Valore non valido")
        if x == 0 or y == 0:
            break
        win = control.controllo(n, m, mines, field, next_matrix)
        if field[x - 1][y - 1].value == '!':
            print_def.print_value(mod, n, m, field)
            print("HAI PERSO")
            break
        if win == 1:
            print_def.print_value(mod, n, m, field)
            print("HAI VINTO!")
            break

    except KeyboardInterrupt:
        print("Interruzione gioco")
        break
