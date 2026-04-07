#Par no ímpar no intervalo
n1 = int(input('Digite um número'))
if (100>=n1>=1):
  if (n1 % 2 == 0):
    print ('Par no intervalo')
  else:
    print ('Ímpar no intervalo')
else:
  print('Fora do intervalo')
