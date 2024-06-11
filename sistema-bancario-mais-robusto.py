class Banco:
    def __init__(self):
        self.usuarios = {}
        self.contas = {}

    def criar_usuario(self, nome, cpf):
        if cpf not in self.usuarios:
            self.usuarios[cpf] = {'nome': nome, 'cpf': cpf}
            print(f"Usuário {nome} criado com sucesso.")
        else:
            print("Usuário já existe.")

    def criar_conta_corrente(self, cpf):
        if cpf in self.usuarios:
            if cpf not in self.contas:
                self.contas[cpf] = ContaCorrente(cpf)
                print(f"Conta corrente para {self.usuarios[cpf]['nome']} criada com sucesso.")
            else:
                print("Conta corrente já existe para este usuário.")
        else:
            print("Usuário não encontrado.")

    def depositar(self, cpf, valor):
        if cpf in self.contas:
            self.contas[cpf].depositar(valor)
        else:
            print("Conta não encontrada.")

    def sacar(self, cpf, valor):
        if cpf in self.contas:
            self.contas[cpf].sacar(valor)
        else:
            print("Conta não encontrada.")

    def extrato(self, cpf):
        if cpf in self.contas:
            self.contas[cpf].extrato()
        else:
            print("Conta não encontrada.")

class ContaCorrente:
    def __init__(self, cpf):
        self.cpf = cpf
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

def interagir_com_cliente():
    banco = Banco()

    while True:
        print("\nSelecione uma opção:")
        print("1. Criar Usuário")
        print("2. Criar Conta Corrente")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Extrato")
        print("6. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            cpf = input("Digite o CPF do usuário: ")
            banco.criar_usuario(nome, cpf)
        elif opcao == "2":
            cpf = input("Digite o CPF do usuário: ")
            banco.criar_conta_corrente(cpf)
        elif opcao == "3":
            cpf = input("Digite o CPF do usuário: ")
            valor = float(input("Digite o valor do depósito: "))
            banco.depositar(cpf, valor)
        elif opcao == "4":
            cpf = input("Digite o CPF do usuário: ")
            valor = float(input("Digite o valor do saque: "))
            banco.sacar(cpf, valor)
        elif opcao == "5":
            cpf = input("Digite o CPF do usuário: ")
            banco.extrato(cpf)
        elif opcao == "6":
            print("Encerrando operação. Obrigado por utilizar nossos serviços. Tenha um bom dia!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    interagir_com_cliente()
