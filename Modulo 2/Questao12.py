def multiplicador(fator):
    def multiplica(numero):
        return numero * fator
    return multiplica

por_dois = multiplicador(2)
print("5 * 2 =", por_dois(5))
