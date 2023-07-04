import math
import os

VALOR_LIMITE_POR_SAQUE = 500
QUANTIDADE_LIMITE_SAQUES_POR_DIA = 3

extrato_bancario = []
saldo_conta = 0.0
quantidade_saques_realizados = 0

def depositar():
    global saldo_conta, extrato_bancario
    valor = float(input('Informe o valor do depósito: R$ '))

    if valor > 0:
        saldo_conta += valor
        extrato_bancario.append(f'Depósito R$ {valor:.2f}')
        print('Depósito realizado com sucesso')
    else:
        print('Não é possível realizar depositos de valores negativos')

def sacar():
    global extrato_bancario, saldo_conta, quantidade_saques_realizados
    
    if quantidade_saques_realizados == QUANTIDADE_LIMITE_SAQUES_POR_DIA:
        print('Limite diário de saques atingido')
    else:    
        valor = float(input('Informe o valor do saque: R$ '))

        if valor > VALOR_LIMITE_POR_SAQUE:
            print(f'O valor máximo permitido por saque é de R$ {VALOR_LIMITE_POR_SAQUE:.2f}')
        elif valor > saldo_conta:
            print('Saldo insuficiente')
        elif valor < 0:
            print('Valor inválido')
        else:
            saldo_conta -= valor
            quantidade_saques_realizados += 1
            extrato_bancario.append(f'Saque R$ {valor:.2f}')
            print('Saque realizado com sucesso')

def emitir_extrato():
    global extrato_bancario, saldo_conta
    
    print('\n********* Extrato Bancário **********\n')
    
    if len(extrato_bancario) == 0:
        print('Não foram realizadas movimentações')
    else:
        for item in extrato_bancario:
            print(item)
        print(f'Saldo R$ {saldo_conta:.2f}')
    
    print('\n*************************************\n')
    

def main():
    os_clear_command = 'nt' if os.name ==  'cls' else 'clear'
    os.system(os_clear_command)
    operacao = 'Z'
    while operacao not in 'xX':

        print(f'"S" para SAQUE\n"D" para DEPÓSITO\n"E" para EXTRATO\n"X" para SAIR')
        operacao = input('Informe a operação desejada: ')

        match operacao:
            case operacao if operacao in 'sS':
                sacar()
            case operacao if operacao in 'dD':
                depositar()
            case operacao if operacao in 'eE':
                emitir_extrato()
            case operacao if operacao in 'xX':
                print('Atendimento finalizado')
                break
            case _:
                print('Operação inválida')
            
main()