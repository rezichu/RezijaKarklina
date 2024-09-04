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
    for masina in masinas:
        print(f"Nosaukums: {masina['nosaukums']}, Marka: {masina['marka']}, Gads: {masina['gads']}")
    #???

def atjaunot_masinu(nosaukums, jauna_marka, jauns_gads):
    for masina in masinas:
        if masina['nosaukums'] == nosaukums:
            masina['marka'] == jauna_marka
            masina['gads'] == jauns_gads
            print(f"Mašīna '{nosaukums}' arjaunināta.")
            return
    print(f"Mašīna '{nosaukums}' nav atrasta sarakstā.")
    #progress 4.septembrī, turpināt 6.septembrī