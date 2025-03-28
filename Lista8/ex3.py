def conversao_entrada():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            print(f"O dobro do número é: {numero * 2}")
            break
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

conversao_entrada()
