# Exer 1

import math

raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio ** 2
print(f"A área do círculo é: {area:.2f}")

# Exer 2

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")

# Exer 3

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
media = (n1 + n2 + n3) / 3
print(f"A média dos três números é: {media:.2f}")

# Exer 4

horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
valor_hora = float(input("Digite o valor recebido por hora: "))
salario = horas_trabalhadas * valor_hora
print(f"O salário total do mês é: R${salario:.2f}")

# Exer 5

metros = float(input("Digite a quantidade em metros: "))
centimetros = metros * 100
print(f"{metros} metros equivalem a {centimetros} centímetros.")



