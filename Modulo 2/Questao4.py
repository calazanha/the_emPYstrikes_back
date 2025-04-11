frase = input("Digite uma frase: ")
vogais = "aeiou"
for vogal in vogais:
    print(f"{vogal}: {frase.lower().count(vogal)}")
print("Frase ao contrário:", frase[::-1])
print("Frase com '-' no lugar de espaços:", frase.replace(" ", "-"))
