gads = int(input('Ievadiet gadu: ')) #:D

for i in range(5,6,1): #Katrus 5 gadus ir garais gads, lai to izrēķinātu izmantoju cikla funkciju
    if gads == 2024 - i or gads == 2024 + i or gads == 2024: #Lai pareizi nosacītu vai garais vai īsais gads
        print(gads,'ir garais gads.')
    else:
        print(gads, 'ir īsais gads.') #Nevaig ar elif, jo var tikai ievadīt veselus skaitļus
