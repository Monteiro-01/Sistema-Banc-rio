import textwrap


def menu():
    menu = """\n
   _______________MENU________________
    [nu]\tNovo usuário
    [nc]\tNova conta
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [lc]\tListar contas
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito: R$ {valor:.2f} \n'
        print('____Deposito feito com sucesso!____')
    else:
        print('____Operação não efetuada! O valor não é valido____')

    return saldo, extrato

def sacar (saldo, valor, extrato, limite, num_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = num_saques >= limite_saques
    
    if excedeu_saldo:
        print('____Operação falhou! Você não tem saldo suficiente.____')

    elif excedeu_limite:
        print('____Operação falhou! O valor do saque excedeu o limite.____')
    
    elif excedeu_saques:
        print('____Operação falhou! Número de saques excedeu.____')

    elif valor > 0:
        saldo -=valor
        extrato += f'Saque: R${valor}\n'
        num_saques += 1
        print('____Saque realizado com sucesso.____')

    return saldo, extrato, num_saques

def exibir_extrato(saldo, extrato):
    print('____________EXTRATO____________')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo: R${saldo:.2f}')
    print('_______________________________')

def criar_usuario(usuarios):
    cpf = input('Informe o seu CPF (apenas números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('____Já existe conta registrada com esse CPF!____')
        return
    
    nome = input('Informe o seu nome completo: ')
    data_nascimento = input('Informe a data de seu nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o seu endereço (logradouro, nº - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco':endereco})

    print('____Usúario criado com sucesso!____')

def filtrar_usuario(cpf, usuarios): 
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf] #comprensão de lista 
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_cont, usuarios):
    cpf = input('Informe o CPF do usúario: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('____Conta criada com sucesso!____')
        return {'agencia': agencia, 'numero_conta': numero_cont, 'usuario': usuario}
    
    print('____Usúario não encontrado, fluxo de criaçao de conta encerrado!____')

def listar_contas(contas):
    for conta in contas: 
        linha = f"""\
            agencia:\t{conta['agencia']}
            c/c:\t\t{conta["numero_conta"]}
            Titular:\t{conta['usuario']['nome']}
        """
        print('='*100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()