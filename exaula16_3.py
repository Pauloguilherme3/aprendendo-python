from random import randint
numero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f"Os valores sorteados foram: {numero[0: 5]}")
print(f"O maior valor foi {sorted(numero)[-1]}")
print(f"O menos valor foi {sorted(numero)[0]}")
