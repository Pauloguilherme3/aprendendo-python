from datetime import datetime
ano = int(input('Digite ano do seu nascimento? '))
genero = str(input('Você e homem ou mulher?"'))
idade = datetime.today().year - ano
print('Quem nasceu em {} tem {} anos !!'.format(ano,idade))
if idade == 18 and genero == "homem":
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade > 18 and genero == "homem":
    print('Você passou do tempo para se alistar devia ter se alistado a {} {} atras.'.format(idade-18,
          "anos"if idade-18 > 1 else "ano"
    ))
    print('Devia ter se alistado no ano {}'.format(ano+18))
elif idade < 18 and genero == "homem":
    print('Você ainda e muito novo , falta {} {} para se alistar.'.format(
        18-idade,"anos" if 18-idade > 1 else "ano"
    ))
    print('Você vai se alistar no ano {}'.format(ano+18))
else:
    print("Você não precisa se alistar!")
