frase = input("Digite uma frase: ").strip().lower()

palavras = frase.split()

contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print("\nContagem de palavras na frase:")
for palavra, quantidade in contagem_palavras.items():
    print(f"'{palavra}': {quantidade}")
