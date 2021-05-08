listagem = ("frango", 10,
            "mouse", 5,
            "lapis", 3.5,
            "caneta", 1.5,
            "mochila", 120.50)
print("="*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("="*40)
for a in range(0, len(listagem), 2):
    print(f"{listagem[a]:.<30}R$ {listagem[a+1]:>6.2f}")
print("="*40)
