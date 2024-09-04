print('Hello World!\n')

#uz ekrāna izdrukāt visus nepāra skaitļus no lietotāja ievadītā diapazona
sakums = int(input("Sākums: "))
beigas = int(input("Beigas: "))

for skaitlis in range(sakums, beigas):
    if  skaitlis%2 != 0:
        print(skaitlis)
