telefons = {'Jānis': 26135132,
            'Rita': 26714236,
            'Anna': 26548253 
        }
#Jānim ir 2 telefona numuri
telefons.update({'Jānis': 22225623})
print('Šis ir Ritas nr.', telefons['Rita'])
print('Šis ir Annas nr.', telefons['Anna'])
print('Šis ir Jāņa nr.', telefons['Jānis'])
print('-------------------------------')

#izveodt vārdnīcu ar atslēgu virkni un fromkeys() metodi
#vārdnīca, nenorādot ierakstu vērtības
kk = ('viens', 'divi', 'trīs')
dd = dict.fromkeys(kk)
print(dd)
val = 0 #šī vērtība būs visai vārdnīcai
dd = dict.fromkeys(kk, val)
print(dd)
print('-------------------------------')

#izveidot vārdnīcu, kas satur sarakstu
valstis = {
    'Somija': ['Helsinki', 'Tampere', 'Rovaniemi'],
    'Norvēģija': ['Oslo', 'Bergena', 'Trumse'],
    'Dānija': ['Kopenhāgena', 'Ronne', 'Odense']
}

for atslega, vertiba in valstis.items():
    for i in vertiba:
        print("{}: {}".format(atslega,i))
    print('🏚🏚🏚')
