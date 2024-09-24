class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_saques_diarios = 3
        self.saques_hoje = 0
        self.limite_valor_saque = 500
        self.mensagem_saque_mostrada = False # Variável para controlar a exibição da mensagem de limite de saques diários.

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"\n\033[32mDepósito de R$ {valor:.2f} realizado com sucesso!\033[0m\n")
        else:
            print("\n\033[31mValor de depósito inválido. O depósito deve ser um valor positivo.\033[0m\n")

    def sacar(self, valor):
        # Mostrar a mensagem de aviso apenas no primeiro saque
        if not self.mensagem_saque_mostrada:
            print(f"\033[33m\n**A sua conta permite realizar três saques diários no valor máximo de R$ 500.00 cada, se houver saldo!")
            self.mensagem_saque_mostrada = True

        if self.saques_hoje >= self.limite_saques_diarios:
            print("\n\033[31mLimite de saques diários atingido.\033[0m\n")
        elif valor > self.saldo:
            print("\n\033[31mSaldo insuficiente para saque.\033[0m\n")
        elif valor > self.limite_valor_saque:
            print(f"\n\033[31mValor de saque excede o limite de R$ {self.limite_valor_saque:.2f} diário por operação.\033[0m\n")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.saques_hoje += 1
            print(f"\n\033[32mSaque de R$ {valor:.2f} realizado com sucesso!\033[0m\n")

    def mostrar_extrato(self):
        print("\n==================== EXTRATO ====================")
        if not self.extrato:
            print("\033[33mNão foram realizadas movimentações.\033[0m")
        else:
            for operacao in self.extrato:
                print(f"\033[34m{operacao}\033[0m")
            print(f"\nSaldo atual: \033[32mR$ {self.saldo:.2f}\033[0m")
        print("==================================================\n")

def mostrar_menu():
    print("\n\033[1;36m==================== MENU ====================\033[0m")
    print("\033[1;36m1\033[0m - Depósito")
    print("\033[1;36m2\033[0m - Saque")
    print("\033[1;36m3\033[0m - Extrato")
    print("\033[1;36m4\033[0m - Sair")
    print("\033[1;36m=============================================\033[0m")

# Criar a conta bancária
conta = ContaBancaria()

# Solicitar o primeiro depósito ao usuário
print("\033[1;33m\nBem-vindo ao seu Banco!\033[0m")
print("\nPara habilitar sua conta é necessário realizar um depósito inicial.")

valor_deposito_inicial = float(input("\nInforme o valor do primeiro depósito: R$ "))
conta.depositar(valor_deposito_inicial)

# Exemplo de como continuar com outras operações
while True:
    mostrar_menu()
    opcao = input("\033[1;36mDigite a opção desejada: \033[0m")

    if opcao == '1':
        valor = float(input("\nInforme o valor do depósito: R$ "))
        conta.depositar(valor)
    elif opcao == '2':
        valor = float(input("\nInforme o valor do saque: R$ "))
        conta.sacar(valor)
    elif opcao == '3':
        conta.mostrar_extrato()
    elif opcao == '4':
        print("\n\033[1;32mObrigado por utilizar nosso sistema bancário! Até a próxima!\033[0m")
        break
    else:
        print("\033[31mOpção inválida. Digite os números correspondentes a operação que deseja realizar.\033[0m")


# Cores do texto na tela:

# \033[32m: Verde para mensagens de sucesso (ex: depósito ou saque realizado com sucesso).
# \033[31m: Vermelho para mensagens de erro (ex: erro no saque ou valor inválido).
# \033[33m: Amarelo para mensagens informativas (ex: quando não há movimentações).
# \033[34m: Azul para as movimentações exibidas no extrato.
# \033[1;36m: Azul claro para o menu e as opções.
