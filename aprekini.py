a = int(input('a= '))
b = int(input('b= '))
darb = input('a,-,*,/:')
if darb == '+':
    c = a + b
elif darb == '-':
    c = a - b
elif darb == '*':
    c = a * b
elif darb == '/':
    c = a / b
else:
    c = 'Kļūda!'
print('Atbilde =', c)