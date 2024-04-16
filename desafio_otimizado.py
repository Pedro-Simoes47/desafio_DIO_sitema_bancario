# Desafio otimizado DIO criando um sistema bancario

import textwrap

def menu():
    menu = """
    Escolha a opcao que deseja executar

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuario
    [5] Criar Conta
    [5] Listar Contas
    [0] Sair


    => """
    return int(input(menu))


def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Valor depositado R$: {valor_deposito:.2f}\n"
        print("Deposito realizado com sucesso!")
    else: 
        print("Operacao falhou! Valor invalido")
    return saldo, extrato

def sacar(*,saldo, valor_saque, extrato, numero_saques, limite_saques):
    exedeu_saldo = valor_saque > saldo

    exedeu_limite = valor_saque > 500

    exedeu_saques = numero_saques >= limite_saques

    if exedeu_saldo:
        print("Saldo Insuficiente!")
            
    elif exedeu_limite:
        print("Exedeu o limite de R$500.00 por saque!")
            
    elif exedeu_saques:
        print("Limite de saques diaros atingido!")

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Valor sacado R$: {valor_saque:.2f}\n"
        numero_saques += 1
        print("Valor sacado com sucesso!")

    else:
        print("Operacao falhou! Valor invalido")
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF para cadastro (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    AGENCIA = "0001"
    saldo = 0.0 
    limite_diario_saque = 1000
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 5
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 1: # DEPOSITO
            valor_deposito = float(input("Informe o valor do deposito: "))
            saldo, extrato = depositar(saldo,extrato)

        elif opcao == 2: # SAQUE
            valor_saque = float(input("Informe o valor que deseja sacar: "))
            saldo, extrato = sacar(saldo=saldo, valor_saque=valor_saque, extrato=extrato, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == 3: # EXTRATO
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4: # Criar usuarios
            criar_usuario(usuarios)

        elif opcao == 5: # Criar Conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6: # Listar Contas
            listar_contas(contas)

        elif opcao == 0: # SAIR
            print()
            break
        
        else:
            print("Opcao Invalida! Digite uma opcao valida.")

main()