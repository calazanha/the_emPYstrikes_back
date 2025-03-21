palavra = input("Digite uma palavra: ").strip()

contagem_caracteres = {}

for letra in palavra:
    if letra in contagem_caracteres:
        contagem_caracteres[letra] += 1
    else:
        contagem_caracteres[letra] = 1

print("\nContagem de caracteres:")
for caractere, quantidade in contagem_caracteres.items():
    print(f"'{caractere}': {quantidade}")
