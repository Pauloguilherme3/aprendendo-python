from datetime import datetime


def voto():
    while True:
        x = (input('Qual ano você nasceu:'))
        try:
            x = int(x)
            if type(x) == int:
                break
        except ValueError:
            print("O valor digitado não e um ano valido , digite o valor correto")
            print(20*"=-")
            continue
    idade = int(datetime.today().year) - x
    if idade < 16:
        print(f"Com {idade} anos o Voto é Negado.")
    elif idade <= 16 or idade > 65:
        print(f"Com {idade} anos o Voto é Opcional.")
    else:
        print(f"Com {idade} anos o Voto é OBRIGATORI.")


voto()
