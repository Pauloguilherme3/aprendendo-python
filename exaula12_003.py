numero = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o Segundo numero: '))
if (numero > numero2):
    print('O primeiro Numero {} e maior'.format(numero))
elif (numero2 > numero):
    print('O segundo Numero {} e maior'.format(numero2))
else:
    print('Os dois numeros são iguais')