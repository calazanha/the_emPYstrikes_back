class SaldoInsuficienteError(Exception):
    pass

def operacoes_bancarias():
    saldo = 1000.00
    try:
        saque = float(input(f"Saldo disponível: R$ {saldo}. Quanto deseja sacar? R$ "))
        if saque > saldo:
            raise SaldoInsuficienteError("Erro: Saldo insuficiente para o saque.")
        saldo -= saque
        print(f"Saque realizado com sucesso. Saldo restante: R$ {saldo}")
    except SaldoInsuficienteError as e:
        print(e)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um valor numérico.")

operacoes_bancarias()
