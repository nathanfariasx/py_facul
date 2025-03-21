# 1. Contagem Progressiva

n = int(input("Digite um número inteiro positivo: "))
for i in range(1, n + 1):
    print(i)

# 2. Soma de Números Positivos

soma = 0
while True:
    numero = int(input("Digite um número positivo (ou negativo para encerrar): "))
    if numero < 0:
        break
    soma += numero
print(f"A soma dos números positivos digitados é: {soma}")

# 3. Tabuada de um Número

n = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 4. Números Ímpares em um Intervalo

a = int(input("Digite o início do intervalo: "))
b = int(input("Digite o fim do intervalo: "))

if a > b:
    a, b = b, a  # Troca para garantir que a <= b

for i in range(a, b + 1):
    if i % 2 != 0:
        print(i)

# 5. Sequência de Fibonacci

n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b