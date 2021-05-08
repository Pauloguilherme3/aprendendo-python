brasileirao = ("America", "Athletico Paranaense", "Atlético", "Atlético",
               "Bahia", "Ceará", "Chapecoense", "Corinthians", "Cuiabá",
               "Flamengo", "Fluminense", "Fortaleza", "Grêmio", "Internacional",
               "Juventude", "Palmeiras", "Red Bull Bragantino", "Santos", "São Paulo", "Sport"
               )
print(f"lista de times do Brasileirao{brasileirao}")
print(f"Os 5 primeiros são {brasileirao[0:5]}")
print(f"Os 4 últimos são {brasileirao[-1:-5:-1]}")
print(f"Times em ordem alfabética: {sorted(brasileirao)}")
print(f"O Chapecoense está na {brasileirao.index('Chapecoense')+1}° posição")
