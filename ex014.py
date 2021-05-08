from random import randint,sample,choice
nome=[]
for i in range(4):
    nome.append(input("Digite nome de um aluno! "))

print(choice(nome))
print(sample(nome,k=4))


