# Sistema Bancário em Python

Este é um projeto de sistema bancário simples desenvolvido em Python. O sistema permite realizar operações básicas, como depósito, saque e visualização de extrato.

## Funcionalidades

O sistema bancário oferece as seguintes funcionalidades:

- Depósito: Permite adicionar valores positivos à conta bancária.
- Saque: Permite realizar até 3 saques diários, com um limite máximo de R$ 500,00 por saque.
- Extrato: Exibe a lista de depósitos e saques realizados, juntamente com o saldo atual da conta.

## Como usar

1. Certifique-se de ter o Python instalado em sua máquina.

2. Faça o download ou clone este repositório em seu ambiente local.

3. Navegue até o diretório do projeto.

4. Execute o arquivo `main.py` para iniciar o sistema bancário.

5. Siga as instruções exibidas no console para realizar as operações desejadas.

## Exemplo de Uso

Aqui está um exemplo básico de uso do sistema bancário:

```python
banco = Banco()
banco.depositar(1000.50)
banco.sacar(200)
banco.sacar(300)
banco.sacar(400)
banco.sacar(150)
banco.depositar(500)
banco.extrato()
```

# Licença

Este projeto está licenciado sob a MIT License.
