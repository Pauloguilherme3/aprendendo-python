from random import randint
numero = int(input("Tente advinhar o numero de 0 a 5 que o Computador esta pensando! "))
sorteio = randint(0,5)
if(numero == sorteio):
    print("Parabens você acertou era o {}!".format(sorteio))
else:
    print("sinto muito nao foi dessa vez! era o {}".format(sorteio))
