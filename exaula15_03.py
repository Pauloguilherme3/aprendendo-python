from random import randint
print("=-"*15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-"*15)
ganhador = 0
while True:
    computador = randint(1,5)
    n = int(input("Diga um valor: "))
    logica = str(input("PAR OU INPAR? [P/I]: ")).strip().upper()
    print("="*40)
    while logica not in "PI":
        print("Digite um valor valido!!")
        logica = str(input("PAR OU INPAR? [P/I]: ")).strip().upper()[0]
    Resultado = "PAR" if (n + computador) % 2 == 0 else "INPAR"
    Resultado1 = "PAR" if logica == "P" else "INPAR"
    if  Resultado1 == Resultado:
        print(f"Você jogou {n} e o computador {computador}. Total deu {n+computador} deu {Resultado}")
        print("="*30)
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
        print("=-"*15)
        ganhador += 1
        continue
    else:
        print(f"Você jogou {n} e o computador {computador}. Total deu {n+computador} deu {Resultado}")
        print("="*30)
        print("Você Perdeu!!")
        print("=-"*15)
        break
print(f"GAME OVER! Você venceu {ganhador} vezes é jogou {ganhador+1} vezes.")
