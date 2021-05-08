nota1 = float(input("Qual a primeira nota?"))
nota2 = float(input("Qual a segunda nota?"))
media = (nota1+nota2)/2
if media < 5:
    print('Reprovado sua media ficou {}'.format(media))
elif 7 > media >= 5:
    print('Recuperação sua media ficou {}'.format(media))
elif media >=7:
    print('Aprovado sua media ficou {}!!'.format(media))
else:
    print('Nota invalida digite uma nota de 0 a 10')