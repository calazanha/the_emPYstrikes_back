try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    print("Resultado da divisão:", a / b)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
