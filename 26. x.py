v1 = int(input('Digite um número: '))
if v1 > 0:
    if v1 <= 10:
        print('Pequeno')
    elif 100 > v1 > 10:
        print ('Médio')
    elif v1 >= 100:
        print ('Grande')
else:
    print ('Negativo ou zero')