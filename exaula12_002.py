import math
numero = int(input('Digite um numero!'))
print("Escolha a conversão!")
print('Digite [1] para binário!')
print('Digite [2] para octal')
print('digite [3] para hexadecimal')
selecionador = int(input('Qual a opção: '))
if selecionador ==1: #converção para binario
    print("O numero {} em binario = {}".format(numero,bin(numero)[2:]))
elif selecionador ==2:
    print("O numero {} em octal = {}".format(numero,oct(numero)[2:]))
elif selecionador ==3:
    print("O numero {} em hexadecimal e = {}".format(numero,hex(numero)[2:]))