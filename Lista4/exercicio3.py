numeros = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))
sem_duplicatas = []
for numero in numeros:
    if numero not in sem_duplicatas:
        sem_duplicatas.append(numero)
print("Lista sem duplicatas:", sem_duplicatas)
