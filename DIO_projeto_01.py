'''Criar um sistema bancário com três operaçôes essenciais: Depósito, saque e extrato.
Saque máximo de R$ 500,00 podendo utilizar a função apenas 3 vezes em um dia com o Total de R$1.500,00'''

funcoes = '''[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair'''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
maximo_saque = 3
while True:
    print(funcoes)
    opcao = input('informe uma opção desejada: ').strip().upper()[0]
    if opcao == 'D':
        print('Depósito')
        try:
            deposito = int(input('Qual valor? '))
            if deposito < 0:
                print('Por favor, insira um valor positivo.')
            saldo += deposito
            extrato += f'Depósito: R${deposito:.2f}\n'
        except ValueError:
            print('Por favor, insira um valor numérico válido.')
    elif opcao == 'S':
        print('Saque')
        numero_saques += 1
        try:
            saque = int(input('Qual é o valor do saque? '))
            if saque < 0:
                print('Por favor, insira um valor positivo.')
            if saque > limite:
                print('Valor acima do limite!')
                if numero_saques > maximo_saque:
                    print('Você excedeu o número maximo de saques por dia.')
        except ValueError:
            print('Por favor, insira um valor numérico válido.')
        else:
            saldo -= saque
            extrato += f'Saque: R${saque:.2f}\n'
    elif opcao == 'E':
        print('Extrado')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSeu saldo é de R${saldo:.2f}')
    elif opcao == 'Q':
        break
    else:
        print('Opção inválida, selecione uma opção existente')
