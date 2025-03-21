times = (
    "Palmeiras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo",
    "Bragantino", "Fluminense", "Athletico-PR", "Internacional", "Fortaleza"
)

print("== Classificação do Campeonato ==")

print("\nTop 3 colocados:")
for i in range(3):
    print(f"{i+1}º - {times[i]}")

print("\nÚltimos 3 colocados:")
for i in range(-3, 0):
    print(f"{len(times) + i + 1}º - {times[i]}")

print("\nTimes em ordem alfabética:")
for time in sorted(times):
    print(f"- {time}")

time_procurado = input("\nDigite o nome de um time para ver sua posição: ").strip()

if time_procurado in times:
    posicao = times.index(time_procurado) + 1  # Índice ajustado para posição
    print(f"O {time_procurado} está na {posicao}ª posição.")
else:
    print("Time não encontrado no top 10 do campeonato.")
