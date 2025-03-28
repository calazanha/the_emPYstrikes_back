def acesso_lista():
    lista = [10, 20, 30, 40, 50]
    try:
        indice = int(input("Digite o índice (0 a 4) para acessar o valor da lista: "))
        print(f"Valor no índice {indice}: {lista[indice]}")
    except IndexError:
        print("Erro: Índice inválido. A lista possui índices de 0 a 4.")
    except ValueError:
        print("Erro: Por favor, digite um número inteiro.")

acesso_lista()
