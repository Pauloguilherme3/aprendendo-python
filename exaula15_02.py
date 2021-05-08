while True:
    print("-"*30)
    n = int(input("Digite qual tabuada voce deseja: "))
    if n < 0:
        print("-"*30)
        break
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
print("Programa tabuada Encerrado ,volte sempre!!")
