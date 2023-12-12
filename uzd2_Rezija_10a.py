datums = {
    '1.decembris': -7, #:D
    '2.decembris': -9,
    '3.decembris': -2,
    '4.decembris': -3,
    '5.decembris': -6,
    '6.decembris': -8,
    '7.decembris': -1
}
reizes = 4
for i in range(1,): 
    a = reizes - i
    while a != 0: #Lai noteiktas reizes iet
        datums_izvele = input('Ievadiet datumu (piem. 5.decembris): ')
        if datums_izvele == '1.decembris':
            print('1.decembrī temperatūra celsija skalā ir: ', datums['1.decembris']) #Katrs datums dabū savu if vai elif
            F = datums['1.decembris'] * (9/5) + 32 #Fērenheita aprēķins (kas dots lapā)
            print('***** \n1.decembrī temperatūra fārenheita skalā ir: ', F, '\n*****')
        elif datums_izvele == '2.decembris':
            print('2.decembrī temperatūra celsija skalā ir: ', datums['2.decembris'])
            F = datums['2.decembris'] * (9/5) + 32
            print('***** \n2.decembrī temperatūra fārenheita skalā ir: ', F, '\n*****') #Zvaigznītes, lai varētu atšķirt datus vienu no otra
        elif datums_izvele == '3.decembris':
            print('3.decembrī temperatūra celsija skalā ir: ', datums['3.decembris'])
            F = datums['3.decembris'] * (9/5) + 32
            print('***** \n3.decembrī temperatūra fārenheita skalā ir: ', F, '\n*****')
        elif datums_izvele == '4.decembris':
            print('4.decembrī temperatūra celsija skalā ir: ', datums['4.decembris'])
            F = datums['4.decembris'] * (9/5) + 32
            print('***** \n4.decembrī temperatūra fārenheita skalā ir: ', F, '\n*****')
        elif datums_izvele == '5.decembris':
            print('5.decembrī temperatūra celsija skalā ir: ', datums['5.decembris'])
            F = datums['5.decembris'] * (9/5) + 32
            print('***** \n5.decembrī temperatūra fārenheita skalā ir: ', F, '\n*****')
        elif datums_izvele == '6.decembris':
            print('6.decembrī temperatūra celsija skalā ir: ', datums['6.decembris'])
            F = datums['6.decembris'] * (9/5) + 32
            print('***** \n6.decembrī temperatūra fārenheita skalā ir: ', F, '\n*****')
        elif datums_izvele == '7.decembris':
            print('7.decembrī temperatūra celsija skalā ir: ', datums['7.decembris'])
            F = datums['7.decembris'] * (9/5) + 32
            print('***** \n7.decembrī temperatūra fārenheita skalā ir: ', F, '\n*****')
        else :
            print('Nepareiza atslēga. Lūdzu, ievadiet datumu no 1. līdz 7.decembra. \n*****') 
