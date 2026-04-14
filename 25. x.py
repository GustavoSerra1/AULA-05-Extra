valor = input('Digite um valor: ')

print(type(valor))

if valor.replace('.', '', 1).isdigit():
    numero = float(valor)
    print(numero / 2)
else:
    print('Não numérico')