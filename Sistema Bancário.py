menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500.00
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Informe o valor do depósito: "))

        if deposito > 0:
    
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        else:
            print("Valor depositado inválido")


    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Informe o valor de saque: "))

            if saque < 0:
                print("Valor de saque inválido")

            if saque > limite:
                print("O limite por saque é de no máximo R$ 500.00")

            elif saque < saldo and saque <= limite:
              
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1

            else:
                print("Não é possivel realizer o saque por saldo insuficiente")

        else:
            print("Você excedeu o numero de saques diários permitidos")


    elif opcao == "e":
        print("\n====================== Extrato ======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: {saldo}")
        print("=====================================================")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")