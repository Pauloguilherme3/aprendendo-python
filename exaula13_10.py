contamulheres= 0
nomehomemvelho =0
somaidade = 0
idadehvelho= 0
for c in range(1,5):
    print("-"*3,"{}°Pessoa".format(c),"-"*3)
    nome= str(input("Qual o nome: ")).strip()
    idade=int(input("Qual a idade: "))
    sexo=str(input("Qual o sexo[M/F]: ")).strip()#M = masculino F= feminino
    somaidade += idade
    if idade < 20 and sexo in "Ff":
            contamulheres += 1
    if idade >  idadehvelho and sexo in "Mm":
        idadehvelho = idade
        nomehomemvelho = nome
print("O {} é o homem mais velho é tem {} anos.".format(nomehomemvelho,idadehvelho))
print("Tem {} mulheres com menos de 20 anos.".format(contamulheres))
print("A idade media e de idade do grupo é {} anos.".format(somaidade/4))
