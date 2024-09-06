#Tukšs saraksts, kur būs mašīnas
masinas = []
def pievenot_masinu(nosaukums, marka, gads):
    masinas.append({
        'nosaukums': nosaukums,
        'marka': marka,
        'gads' : gads
    })
    print(f"Mašīna '{nosaukums}' pievienota sarakstam")

def paradit_masinas():
    if masinas:
        print('\nMašīnas sarakstā: ')
        for masina in masinas:
            print(f"Nosaukums: {masina['nosaukums']}, Marka: {masina['marka']}, Gads: {masina['gads']}")
    else:
        print('\nSaraksts ir tukšs.')

def atjaunot_masinu(nosaukums, jauna_marka, jauns_gads):
    for masina in masinas:
        if masina['nosaukums'] == nosaukums:
            masina['marka'] == jauna_marka
            masina['gads'] == jauns_gads
            print(f"Mašīna '{nosaukums}' arjaunināta.")
            return
    print(f"Mašīna '{nosaukums}' nav atrasta sarakstā.")
    #progress 4.septembrī, turpināt 6.septembrī

def dzest_masinu(nosaukums):
    for masina in masinas:
        if masina['nosaukums'] == nosaukums:
            masinas.remove(masina)
            print(f"Mašīna '{nosaukums}' dzēsta no saraksta.")
            return
    print(f"Mašīna '{nosaukums}' nav atrasta sarakstā.")

while True:
    print('\nIzvēlies darbību:')
    print('1. Pievienot mašīnu')
    print('2. Parādīt visas mašīnas')
    print('3. Atjaunināt mašīnu')
    print('4. Dzēst mašīnu')
    print('5. Iziet')

    izvele = input('Izvēlies darbību(1-5): ')
    if izvele == '1':
        nosaukums = input('Ievadiet mašīnas nosaukumu: ')
        marka = input('Ievadiet mašīnas marku: ')
        gads = input('Ievadiet mašīnas gadu: ')
        pievenot_masinu(nosaukums, marka, gads)

    elif izvele == '2':
        paradit_masinas()

    elif izvele == '3':
        nosaukums = input('Ievadiet nosaukumu, kuru vēlaties atjaunot: ')
        jauna_marka = input('Ievadiet jaunu marku: ')
        jauns_gads = input('Ievadiet jauno mašīnas gadu: ')
        atjaunot_masinu(nosaukums, jauna_marka, jauns_gads)
    
    elif izvele == '4':
        nosaukums = input('Ievadiet nosaukumu mašīnai, ko vēlaties dzēst no saraksta: ')
        dzest_masinu(nosaukums)

    elif izvele == '5':
        print('Programma beidzas. Atā! ♪(´▽｀)')
        break

    else:
        print('Nepareiza ievade.')
