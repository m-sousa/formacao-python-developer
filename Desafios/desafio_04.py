import math

VALOR_LIMITE_POR_SAQUE = 500
QUANTIDADE_LIMITE_SAQUES_POR_DIA = 3

depositos_realizados = []
saques_realizados = []

saldo_conta = 0.0

def sacar(valor):
    global saques_realizados, saldo_conta

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

def depositar():
    global saldo_conta, depositos_realizados
    valor = float(input('Informe o valor do depósito: R$ '))

    if valor > 0:
        saldo_conta += valor
        depositos_realizados.append(valor)
        print('Depósito realizado com sucesso')
    else:
        print('Não é possível realizar depositos de valores negativos')

def emitir_extrato():
    imprimir_depositos()
    imprimir_saques()

def imprimir_depositos():
    global depositos_realizados
    if len(depositos_realizados) > 0:
        for d in depositos_realizados:
            print(f'R$ {d:.2f} ')

def imprimir_saques():
    global saques_realizados
    if len(saques_realizados) > 0:
        for d in saques_realizados:
            print(f'R$ {d:.2f} ')


def main():
    operacao = 'Z'

    while operacao not in 'sS':
        print(f'"S" para SAQUE\n"D" para DEPÓSITO\n"E" para EXTRATO\n"X" para SAIR')
        operacao = input('Informe a operação desejada: ')

        match operacao:
            case operacao if operacao in 'sS':
                sacar()
            case operacao if operacao in 'dD':
                depositar()
            case operacao if operacao in 'eE':
                emitir_extrato()
            case operacao if operacao in 'sS':
                break
            
main()