import math
import random

num = float(input("Digite um número para calcular a raiz quadrada: "))
print("Raiz quadrada:", math.sqrt(num))
print("Número aleatório entre 1 e 100:", random.randint(1, 100))

# 2. Uso do Módulo platform
import platform
print("Sistema operacional:", platform.system())
print("Versão do sistema:", platform.version())
print("Arquitetura:", platform.architecture())
