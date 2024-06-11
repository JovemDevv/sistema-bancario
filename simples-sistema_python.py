class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.saques_realizados = []
        self.depositos_realizados = []

    def depositar(self, valor):
        if valor > 0:
            self.depositos_realizados.append(valor)
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido. O depósito deve ser um valor positivo.")

    def sacar(self, valor):
        if self.saldo >= valor and valor <= 500.00 and len(self.saques_realizados) < 3:
            self.saques_realizados.append(valor)
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif valor > 500.00:
            print("Valor inválido. O valor máximo de saque é R$ 500.00.")
        elif len(self.saques_realizados) >= 3:
            print("Limite máximo de saques diários atingido.")
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        if len(self.depositos_realizados) == 0 and len(self.saques_realizados) == 0:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in self.depositos_realizados:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques_realizados:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")


# Função para interagir com o cliente
def interagir_com_cliente():
    banco = Banco()

    while True:
        print("Selecione uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))
            banco.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: "))
            banco.sacar(valor)
        elif opcao == "3":
            banco.extrato()
        elif opcao == "4":
            print("Encerrando operação. Obrigado por utilizar nossos serviços. Tenha um bom dia!")

            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


# Executar interação com o cliente
interagir_com_cliente()
