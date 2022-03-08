def iterativehelp():
    while True:
        print("\033[45;30m", 12*"-=", "\033[0m")
        print("\033[45;30m  SISTEMA DE AJUDA PYHELP","\033[0m")
        print("\033[45;30m", 12*"-=", "\033[0m")
        funcao = input("Digite funcao ou biblioteca:")
        if funcao.capitalize() == "Fim":
            print(f"\033[42m {6*'-='} \033[m")
            print("\033[42m   Ate logo   \033[m")
            print(f"\033[42m {6*'-='} \033[m")
            break
        try:
            print("\033[43;30m", 16*"-=", "\33[0m")
            print(f"\033[43;30m  Acessando o manual de comando {funcao}\033[0m")
            print(f"\033[42;30m {help(funcao)} \033[0m")
        except ValueError:
            print("\033[45;30 nao corresponde a uma string")

iterativehelp()
