def calcular_media(lista):
    return sum(lista) / len(lista)
numeros = list(map(int, input("Digite números separados por espaço: ").split()))
media = calcular_media(numeros)
print(f"A média dos números inseridos é: {media}")
