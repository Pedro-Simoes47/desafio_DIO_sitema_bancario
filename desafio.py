# Desafio DIO criando um sistema bancario


menu = """
    Escolha a opcao que deseja executar

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair


=> """

saldo = 0.0 
limite_diario_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1: # DEPOSITO
        valor_deposito = float(input("Informe o valor do deposito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Valor depositado R$: {valor_deposito:.2f}\n"
        else: 
            print("Operacao falhou! Valor invalido")

    elif opcao == 2: # SAQUE
        valor_saque = float(input("Informe o valor que deseja sacar: "))
        exedeu_saldo = valor_saque > saldo

        exedeu_limite = valor_saque > 500

        exedeu_saques = numero_saques >= LIMITE_SAQUES

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
        
        else:
            print("Operacao falhou! Valor invalido")

    elif opcao == 3: # EXTRATO
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 0: # SAIR
        print()
        break
    
    else:
        print("Opcao Invalida! Digite uma opcao valida.")