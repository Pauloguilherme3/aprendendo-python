from random import randint
computador = randint(1,10)
contador = 0
jogador = 0
print("Sou seu computador... \nAcabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
while computador != jogador:
    jogador = int(input("Qual é seu palpite: "))
    if jogador > computador:
        print("Menos.. Tente mais uma vez")
    elif jogador < computador:
        print("Mais.. Tente mais uma vez")
    contador += 1
print("PARABENS, Você acertou!!")
print("Você precisou de {} tentativas para acertar".format(contador))