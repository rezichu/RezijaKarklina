import math
import random

rl = int(input('Ievadiet riņķa līnijas rādiusu: ')) #rl ievadītais riņķa līnijas rādiuss
print(rl)
print(float(rl))

pi = float(3.1416)
rlg = 2 * pi * rl #rlg ir rinķa līnijas garums
rll = pi * rl *rl #rll ir rinķa l;inijas laukums
print('Rinķa līnijas garums: ' "{:.2f}".format(rlg))
print('Rinķa līnijas laukums: ' "{:.2f}".format(rll))

k1 = int(input('Ievadiet taisnleņķa katešu garumu: ')) #k1 ir ievadītais katešu garums
print(k1)
k2 = int(input('Ievadiet otrās katetes garumu: ')) #k2 ir ievadītais katešu garums
hg = ((k1*2) * (k2*2)) / 2
print('Taisnleņķa trijstūra hipotenūzas garums: ', hg)

gs = random.random()
print("Gadījuma skaitlis no 0 - 1:", gs)