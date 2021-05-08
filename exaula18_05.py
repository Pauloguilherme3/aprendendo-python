aluno = [[], []]
nome = []
nota = []
while True:
    nome.append(str(input('Digite o nome do aluno: ')))
    for i in range(2):
        nota.append((str(input(f'Nota {i + 1}: '))))
    aluno[0].append(nome[:])
    aluno[1].append(nota[:])
    nome.clear(), nota.clear()
    controle = str(input('Quer continuar?[S/N]')).upper().strip()
    if controle == 'N':
        break
print(f'{"No.":<4}{"NOME":<20}{"MEDIA":>8}')
for d in range(len(aluno[0])):
    media = ((float(aluno[1][d][0]) + float(aluno[1][d][1])) / 2)
    print(f'{d:<2}  {aluno[0][d][0]:<20}{media:^10}')
print('=' * 40)
while True:
    m = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if m == 999:
        print('Volte sempre')
        break
    if m <= len(aluno[0]) - 1:
        print(f'As notas de {aluno[0][m][0]} são {aluno[1][m]}')
