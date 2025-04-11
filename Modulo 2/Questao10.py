def contar_pares(n):
    for i in range(0, n+1, 2):
        yield i

limite = int(input("Mostrar pares até: "))
for num in contar_pares(limite):
    print(num)
