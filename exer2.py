# Exer 1

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# Exer 2

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print(f"O maior número é: {n1}")
elif n2 > n1:
    print(f"O maior número é: {n2}")
else:
    print("Os dois números são iguais.")


# Exer 3

idade = int(input("Digite a idade: "))

if idade < 18:
    print("Menor de idade")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")

# Exer 4

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Aprovado com média {media:.2f}")
elif media >= 5:
    print(f"Recuperação com média {media:.2f}")
else:
    print(f"Reprovado com média {media:.2f}")

# Exer 5

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os lados formam um triângulo válido.")
else:
    print("Os lados não formam um triângulo válido.")

