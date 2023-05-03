menu = '''
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> '''

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3   

while True:
    
    opcao = input(menu)

    if opcao.upper() == "D":
        valor = float(input("Olá, informe o valor do depósito: "))

        if (valor > 0): 
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Erro! Operação falhou, valor inválido.")

    elif opcao.upper() == "S":
        valor = float(input("Olá, informe o valor do saque: "))
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES 
        excedeu_saldo  = valor > saldo 
        excedeu_limite_diario = valor > limite 

        if(excedeu_saques):
            print("Operação falhou. \n Sinto muito, você excedeu o limite de saques diário.")
        elif(excedeu_limite_diario):
            print("Operação falhou. \n Sinto muito, o valor excede o limite.")
        elif(excedeu_saldo):
            print("Operação falhou. \n Salfo insuficiente.")
        elif(valor > 0):
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou. \n O valor informado é inválido.")

    elif opcao.upper() == "E":
        print("Extrato".center(30, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'Seu saldo é R${saldo:.2f}')
        print("=".center(29, "="))

    elif opcao.upper() == "Q":
        break

    else:
        print("Operação inválida.")