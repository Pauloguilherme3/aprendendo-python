print("=" * 30)
txt = "Banco CEV"
print(f"{txt:^30}")
print("=" * 30)
nota = 50
qnotas = 0
valorsacar = int(input("Qual valor deseja sacar: R$"))
while True:
    if valorsacar >= nota:
        valorsacar -= nota
        qnotas += 1
    else:
        if qnotas > 0:
            print(f"Total de {qnotas} notas de R${nota}")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        qnotas = 0
        if valorsacar == 0:
            break
print("="*30)
print(f"Volte Sempre ao {txt}! Tenha um bom dia!")
