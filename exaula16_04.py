maisde18 = homenscadastrados = idademulheresmenosde20 = 0
while True:
    print("="*30)
    print("CADASTRE UMA PESSOA")
    print("="*30)
    idade = int(input("Digite sua idade:"))
    sexo = " "
    while sexo not in 'FM':
        sexo = str(input("Sexo [M/F]")).strip().upper()
        print("=" * 30)
    if sexo == "F" and idade < 20:
        idademulheresmenosde20 += 1
    if sexo == "M":
        homenscadastrados += 1
    if idade >= 18:
        maisde18 += 1
    controle = " "
    while controle not in "SN":
        controle = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if controle == "N":
        break
print("="*6, " FIM DO PROGRAMA ", "="*6)
print(f"Tem {maisde18} pessoas acima de 18 anos")
print(f"Tem {homenscadastrados} homems cadrastrados")
print(f"Tem {idademulheresmenosde20} mulheres com menos de 18 anos")
