"""
Escreva um programa que peça um número inteiro positivo ao usuário e exiba todos os
números de 1 até esse número, um por linha.
"""
x = int(input("Insira um número inteiro: "))
for c in range(x):
    print(c+1, end="\n")
