# 1. Divisão Segura

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
else:
    print(f"Resultado da divisão: {resultado}")

# 2. Abertura Segura de Arquivo

try:
    nome_arquivo = input("Digite o nome do arquivo: ")
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:\n")
        print(conteudo)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")

# 3. Conversão de Entrada com Exceções

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"O dobro de {numero} é {numero * 2}")
        break
    except ValueError:
        print("Erro: Digite um número inteiro válido.")

# 4. Acesso a Elementos de uma Lista

lista = [10, 20, 30, 40, 50]

try:
    indice = int(input("Digite um índice (0 a 4): "))
    print(f"O valor no índice {indice} é {lista[indice]}")
except IndexError:
    print("Erro: Índice fora do intervalo da lista.")
except ValueError:
    print("Erro: Por favor, digite um número inteiro.")

# 5. Operações Bancárias com Tratamento de Erros

class SaldoInsuficienteError(Exception):
    pass

saldo = 1000.00

try:
    saque = float(input("Digite o valor para saque: "))
    if saque > saldo:
        raise SaldoInsuficienteError("Erro: Saldo insuficiente para realizar o saque.")
    saldo -= saque
    print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
except ValueError:
    print("Erro: Valor inválido. Digite um número.")
except SaldoInsuficienteError as e:
    print(e)
