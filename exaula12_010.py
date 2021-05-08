from random import randint
from time import sleep
jogo = ["Pedra","Papel","Tesoura"]
jogador = int(input("""     Qual escolha uma alternativa!
Digite [1] para Pedra 
Digite [2] para Papel
Digite [3] para Tesoura
Qual sua escolha? """))
print("Jo")
sleep(1)
print("ken")
sleep(1)
print("PO!!")
escolha = jogo[jogador-1]
computador = jogo[randint(0,2)]
if (escolha == "Pedra"   and computador == "Tesoura" or
    escolha == "Papel"   and computador == "Pedra"   or
    escolha == "Tesoura" and computador == "Papel"):
    print("Você ganhou, você {} e o computador {}".format(escolha,computador))
elif(escolha == computador):
    print("Empate")
else:
    print("Voce Perdeu, você {} e o computador {}".format(escolha,computador))

