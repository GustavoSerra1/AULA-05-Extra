#xx
n1 = input('Digite um número:')
if n1.isnumeric():
    n1 = int(n1)
    if n1 > 10:
        print ('Alto')
    else:
        print ('Baixo')
else:
    print ('Entrada Inválida')
#CÓDIGO NÃO ACEITA NÚMERO QUEBRADO OU NEGATIVO (NAO SEI FAZER DIFERENTE)
