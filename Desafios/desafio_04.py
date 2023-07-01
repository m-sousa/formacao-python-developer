import math

VALOR_LIMITE_POR_SAQUE = 500
QUANTIDADE_LIMITE_SAQUES_POR_DIA = 3

depositos_realizados = []
saques_realizados = []

saldo_conta = 0

def sacar(valor):
    if len(saques_realizados) == QUANTIDADE_LIMITE_SAQUES_POR_DIA:
        print('Limite diário de saques atingido')
    elif valor > VALOR_LIMITE_POR_SAQUE:
        print('O valor máximo permitido por saque é de R$ 500.00')
    elif valor > saldo_conta:
        print('Saldo insuficiente')
    else:
        saldo_conta -= valor
        saques_realizados.append(valor)
        print('Saque realizado com sucesso')

def depositar(valor):
    if valor > 0:
        saldo_conta += valor
        depositos_realizados.append(valor)
        print('Depósito realizado com sucesso')
    else:
        print('Não é possível realizar depositos de valores negativos')

def emitir_extrato():
    print('''### EXTRATO BANCÁRIO ###
    ''')