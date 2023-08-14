from time import sleep

def linha():
    print('='*50)

def cabeçalho():
    linha()
    print('Bem vindo ao Banco Ismael!'.center(50))
    linha()

def depositar():
    valor_deposito=float(input('Digite o valor desejado: '))
    saldo+=valor_deposito
    extrato+=valor_deposito
    return f'Depósito de R${valor_deposito:.2f} efetuado com sucesso! Saldo Atual R${saldo:.2f}.'


def sacar():
    valor_saque=float(input('Digite o valor desejado:'))
    saldo-=valor_saque
    extrato+=valor_saque
    return f'Saque de R${valor_saque:.2f} efetuado com sucesso. Saldo atual: R${saldo:.2f}.'


def extrato():
    linha()
    print('Extrato de Conta Bancária'.center(50))
    linha()
    print(f'''\n{extrato}
            \nValor total de Depósitos:R${valor_total_depositos:.2f}
            \nValor total de saques:R${valor_total_saques:.2f}
            \nSaldo Disponível: R${saldo:.2f}''')
    sleep(2)



def saldo():
    linha()
    print(f'Seu saldo atual é: R${saldo:.2f}')
    linha()
    sleep(2)


def NovaConta():


def listarContas():






numero_de_saques=0
limite_de_saques=3
valor_total_saques=0
valor_total_depositos=0
extrato=''
saldo=0
limite=500
while True:
    cabeçalho()
    menu=int(input('''MENU PRINCIPAL
    \n[1]-Depósito
    \n[2]-Saque
    \n[3]-Extrato
    \n[4]-Saldo
    \n[5]-Nova Conta
    \n[6]-Listar Contas
    \n[7]-Novo usuário               
    \n[5]-Sair
    \nDigite a operação desejada:'''))

    if menu==1:
        
        print(f'\033[1;31;42m Deposito de R${valor_deposito:.2f} efetuado com sucesso! \033[m')
        print(f'Seu saldo atual é:R${saldo:.2f}')
        
        
    elif menu==2:        
        
        print('\033[1;30;41m Operação falhou!Valor informado excede o saldo disponível para saque.\033[m')
    
        print('\033[1;30;41m Valor Inválido! INFORME UM VALOR VÁLIDO! \033[m')
    
        print('\033[1;30;41m Operação falhou!Valor informado excede o limite para saque.\033[m')
    
        print('\033[1;30;41m Operação falhou!Você excedou o número diário para saques.')
    
        print(f'\033[1;31;42m Saque de R${valor_saque:.2f} efetuado com sucesso! \033[m')
        
        
    elif menu==3:
        print('\033[1;31;42m Obrigado por usar os serviços do Banco Ismael!\n Até a próxima.\033[m')
        
        print('\033[1;30;41m Opção inválida! Tente novamente.\033[m')
        

