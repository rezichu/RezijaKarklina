saraksts = [1,2,7,8,5,3,5,5,2,2] #:D

print('Saraksts: ',saraksts)
para_skaitli = [num for num in saraksts if num%2 == 0] #Izņem pāra skaitļus no saraksta
print('Pāra skaitļu skaits:', len(para_skaitli)) #Saskaita pāra skaitļus (skaits)
nepara_skaitli = [num for num in saraksts if num%2 != 0] #Izņem nepāra skaitļus no saraksta
print('Nepāra skaitļu skaits:',len(nepara_skaitli)) #Saskaita nepāra skaiļus (skaits)