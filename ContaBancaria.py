from time import sleep
import textwrap

def linha():
    print('='*50)

def cabeçalho():
    linha()
    print('Bem vindo ao Banco Ismael!'.center(50))
    linha()

def menu():
    cabeçalho()
    print("MENU PRINCIPAL".center(50))
    linha()
    menu=int(input('''
    \t[1]-Depósito
    \t[2]-Saque
    \t[3]-Extrato
    \t[4]-Criar Usuário
    \t[5]-Nova Conta
    \t[6]-Listar Contas
    \t[7]-Sair               
    \tDigite a operação desejada:'''))
    return menu

def depositar(saldo,valor_deposito, extrato,/):
    if valor_deposito>0:
        saldo+=valor_deposito
        extrato+=f'Depósito:\t\tR${valor_deposito:.2f}\n'
        print(f'\nDepósito de R${valor_deposito:.2f} efetuado com sucesso!')
    else:
        print('\033[1;30;41 OPERAÇÂO FALHOU! O Valor informado é Inválido! \033[m')

    return saldo,extrato


def sacar(*,saldo, valor_saque,extrato,limite_saque,numero_saques,limite,total_saques):
    if valor_saque>saldo:
        print('\033[1;30;41m Operação falhou!Valor informado excede o saldo disponível para saque.\033[m')
    elif valor_saque<=0:
        print('\033[1;30;41m Valor Inválido! INFORME UM VALOR VÁLIDO! \033[m')
    elif valor_saque>limite:
        print('\033[1;30;41m Operação falhou!Valor informado excede o limite para saque.\033[m')
    elif numero_saques>=limite_saque:
        print('\033[1;30;41m Operação falhou!Você excedeu o número diário para saques.')
    else:
        print(f'\033[1;31;42m Saque de R${valor_saque:.2f} efetuado com sucesso! \033[m')
        numero_saques+=1
        saldo-=valor_saque
        total_saques+=valor_saque
        extrato+= f'Saque:\t\tR$ {valor_saque:.2f}\n'
    return saldo, extrato
   

def extrato(total_depositos,total_saques,saldo):
    linha()
    print('Extrato de Conta Bancária'.center(50))
    linha()
    print('Não foram realizadas movimentações.'if not extrato else extrato)
    print(f'''\n{extrato}
            \nValor total de Depósitos:\tR${total_depositos:.2f}
            \nValor total de saques:\tR${total_saques:.2f}
            \nSaldo Disponível: \tR${saldo:.2f}''')
    sleep(2)
def criar_usuario(usuarios):
    cpf=input('Informe o CPF(Somente números): ')
    usuario=filtrar_usuario(cpf,usuarios)

    if usuario:
        print('\n Já existe usuário com este CPF!')
        return
    nome=input('Informe o Nome completo: ')
    data_nascimento=input('Infome a data de nascimento (dd-mm-aaaa): ')
    endereço=input('Infome o endereço(logradouro,n°-bairro-Cidade/sigla estado:): ')

    usuarios.append({'nome':nome,'data_nascimento':data_nascimento,'cpf':cpf,'endereço': endereço})
    print('\033[1;30;41 Usuário criado com sucesso!!\033[m')

def filtrar_usuario(cpf,usuarios):
    usuarios_filtratdos=[usuario for usuario in usuarios if usuario['cpf']==cpf]
    return usuarios_filtratdos[0] if usuarios_filtratdos else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf=input('Informe o CPF do usuário: ')
    usuario=filtrar_usuario(cpf,usuarios)
    if usuario:
        print('\n### Conta Criada com Sucesso! ###')
        return {'agencia':agencia,'numero_conta':numero_conta, 'usuario': usuario}
    print('\n USUÀRIO NÃO ENCONTADO! Fluxo de Criação de conta Encerrado!')


def listar_contas(contas):
    for conta in contas:
        linha= f'''\
        Agencia:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        '''
        print('x'*100)
        print(textwrap.dedent(linha))
        


def sair():
    linha()
    print('\033[1;31;42m Obrigado por usar os serviços do Banco Ismael!\n Até a próxima.\033[m')
    linha()

def main():
    LIMITE_SAQUES=3
    AGENCIA='0001'
    numero_conta=0
    numero_saques=0
    total_saques=0
    total_depositos=0
    extrato=''
    saldo=0
    limite=500
    usuarios=[]
    contas=[]
    while True:
        opcao=menu()        
        if opcao==1:
            valor_deposito=float(input('Informe o valor do depósito: '))
            saldo,extrato=depositar(saldo,valor_deposito,extrato)
            
        elif opcao==2:        
           valor_saque=float(input('Informe o valor do saque: '))
           saldo,extrato= sacar(saldo=saldo,
                                valor_saque=valor_saque,
                                extrato=extrato,
                                limite=limite,
                                numero_saques=numero_saques,
                                limite_saque=LIMITE_SAQUES,
                                total_saques=total_saques
                                )
        elif opcao==3:
            extrato(saldo,extrato=extrato)
        elif opcao==4:
            criar_usuario(usuarios)
        elif opcao==5:
            criar_conta=len(contas)+1
            conta=criar_conta(AGENCIA,numero_conta,usuarios)
            if conta:
                contas.append(conta)
        elif opcao==6:
            listar_contas()            

        elif opcao==7:
            print('\033[1;31;42m Obrigado por usar os serviços do Banco Ismael!\n Até a próxima.\033[m')
        else:
            print('\033[1;30;41m Opção inválida! Tente novamente.\033[m')

main()