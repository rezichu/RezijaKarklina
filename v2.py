'''atbilde = 'j'
while atbilde == 'j':
    print('Nekusties!')
    atbilde = input('Vai briesmonis ir draudzīgs?(j/n): ')
print('Bēdz prom!')'''

#pārbaudīt vai lietotājs prot reizrēķinu līdz 7
#programma atkārto darbību līdz brīdim, kad uzdoti visi 12 jautājumi
reiz = 7
for i in range(1,13): #cikla mainīgais no 1 - 12
    print('Cik ir', i, 'x', reiz, '?')
    minejums = input()
    if minejums == 'stop':
        break #pārtrauc ciklu
    if minejums == 'izlaist':
        print('Tiek izlaists!')
        continue
    atb = i * reiz
    if atb == int(minejums):
        print('Pareizi!')
    else:
        print('Nē, tas ir ', atb,'!')

