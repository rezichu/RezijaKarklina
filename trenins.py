nenodots = input('Vai Jums ir kāds laikā nenodots izdevums? (j/n)')
if nenodots == 'j':
    print('Jūs nedrīkstat neko saņemt!')
elif nenodots == 'n':
    pieprasits = input('Vai izdevums ir pieprasīts?')
    if pieprasits == 'j':
        print('Izsniedz uz 2 dienām!')
    elif pieprasits == 'n':
        zurnals = input('Vai publikācija ir žurnāls?')
        if zurnals == 'j':
            print('Izsniedz uz 7 dienām!')
        elif zurnals == 'n':
            persona = input('Vai jūs esat students?')
            if persona == 'j':
                print('Izsniedz uz 14 dienām!')
            elif persona == 'n':
                print('Izsniedz uz 14 dienām!')
else:
    exit()