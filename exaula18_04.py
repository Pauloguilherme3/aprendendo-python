from random import randint
from time  import sleep
# from pygame.time import delay
print("="*40)
print(f'{"O jogo da mega sena":^40}')
print("="*40)
jogo = []
n = int(input("Quantos jogos? "))
print("-="*3, f"SORTEANDO {n} JOGOS", "-="*3)
for jogos in range(n):
    while True:
        fd = randint(1, 60)
        if fd not in jogo:
            jogo.append(fd)
        if len(jogo) == 6:
            break
    print(f'jogo {jogos+1}:{jogo}')
    sleep(1)
    jogo.clear()
print('-='*5, ' < BOA SORTE! > ', "-="*5)
