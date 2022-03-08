def ficha():
    print(30*"=")
    jogador = input("Nome do Jogador:")
    gols = input("Quantos Gols:")
    if jogador.strip() == "" or jogador.isnumeric():
        jogador = "<desconhecido>"
    if not gols.isnumeric():
        gols = 0
    print(f"O jogador {jogador} fez {gols} Gol(s) no campeonato.")


ficha()
