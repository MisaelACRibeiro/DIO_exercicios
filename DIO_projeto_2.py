def menu():
    menu = '''\n[D] Depositar
[S] Sacar
[E] Extrato
[NC] Nova Conta
[LC] Listar Contas
[NU] Novo usuário
[Q] Sair
Digite uma opção: '''
    return input(menu).strip().upper()
def depositar(saldo, deposito, extrato, /):
    if deposito < 0:
        print('Por favor, insira um valor positivo.')
    saldo += deposito
    extrato += f'{"Depósito":.<20} R${deposito:.2f}\n'
    return saldo, extrato
def sacar(*, saque, limite, saldo, extrato, numero_saques, maximo_saque):
    if saque > saldo:
        print('Saldo insuficiente.')
    elif saque < 0:
        print('Por favor, insira um valor positivo.')
    elif saque > limite:
        print('Valor acima do limite!')
    elif numero_saques > maximo_saque:
        print('Você excedeu o número máximo de saques por dia.')
    else:
        saldo -= saque
        extrato += f'{"Saque":.<20} R${saque:.2f}\n'
    return saldo, extrato
def exibir_extrato(saldo, /, *, extrato):
    print('=' * 30)
    print(f'{"Extrado":^30}')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print('=' * 30)
    print(f'{"Saldo":.<20} R${saldo:.2f}\n')
def criar_usuario(usuarios):
    cpf = input('Informe o CPF (apenas números): ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('CPF existente!')
        return
    nome = input('Nome completo: ').title()
    data_nascimento = input('Data de Nascimento (DD-MM-AAAA): ')
    endereço = input('Endereço (Rua, Número, Bairro, Cidade/sigla estado): ')
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereço': endereço})
    print(f'{"Sucesso":^30}')
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print(f'{"Sucesso":^30}')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print('CPF não encontrado')
def listar_contas(contas):
    for conta in contas:
        linha = f"""Agência:{conta['agencia']}\nC/C:{conta['numero_conta']}\nTitular:{conta['usuario']['nome']}"""
        print(linha)
def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    maximo_saque = 3
    agencia = '0001'
    usuarios = []
    contas = []
    while True:
        funcoes = menu()
        if funcoes == 'D':
            print('Depósito')
            deposito = int(input('Qual valor? '))
            saldo, extrato = depositar(saldo, deposito, extrato)
        elif funcoes == 'S':
            print('Saque')
            saque = int(input('Qual é o valor do saque? '))
            saldo, extrato = sacar(saque=saque, limite=limite, saldo=saldo, extrato=extrato, numero_saques=numero_saques, maximo_saque=maximo_saque)
        elif funcoes == 'E':
            exibir_extrato(saldo, extrato=extrato)
        elif funcoes == 'NU':
            print('Criar novo usuário')
            criar_usuario(usuarios)
        elif funcoes == 'NC':
            print('Criando nova conta')
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif funcoes == 'LC':
            print('Listas de Contas Cadastradas')
            listar_contas(contas)
        elif funcoes == 'Q':
            break
        else:
            print(f'{" ERRO ":*^30}')
            print("Operação inválida, por favor selecione novamente a operação desejada.")
main()
