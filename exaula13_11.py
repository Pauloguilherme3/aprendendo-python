from datetime import date
ano = []*8
contador =0
for c in range(1,8):
    ano = int(input("Digite ano que a {}° nasceu:".format(c)))
    idade = date.today().year - ano
    if idade >= 18:
        contador+=1
print("Possui {} pessoas que atingiu a maioridade !!".format(contador))
print("E {} pessoas que ainda não atingiram a maior idade !!".format(7-contador))

