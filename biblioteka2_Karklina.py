paradi = input('Vai ir parādi? (j/n): ')

if paradi == 'j':
    print('Nevar izdevumu saņemt!')
    exit()
elif paradi == 'n':
    veids = input('Vai ir pieprasīts? (j/n):')
    if veids == 'j':
        print('Izdevumu izdod uz 2 dienām!')
    elif veids == 'n':
        izdevums = input('Grāmata vai žurnāls? (g/z): ')
        if izdevums == 'z':