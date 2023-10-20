'''Pirmie 2 suņa gadi = 10.5 cilvēka gadi
Pārējie gadi ir salīdzinami ar 4 cilvēka gadiem
ievadītie gadi nevar būt mazāki par 0'''

sg = int(input('Ievadiet suņa gadus: '))


if sg <= 2:
    cg = sg*10.5
    print('Cilvēka gados:',cg)
elif sg > 2:
    cg = sg*4
    print('Cilvēka gados:',cg)
elif sg <= 0:
    exit()
else:
    print('Ievadiet pareizos datus!')


'''cilveks = int(input("Ievadiet suņa vecumu cilvēka gados: "))

if cilveks < 0:
    print("Vecumam jābūt lielākam par 0.")
    exit()
elif cilveks <= 2:
    suns_vecums = cilveks * 10.5
else:
    suns_vecums = 21 + (cilveks - 2)*4

print("Suņa vecums suņa gados ir: ", suns_vecums)'''