# 1. Cálculo do Fatorial

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Digite um número inteiro para calcular o fatorial: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")

# 2. Verificação de Número Primo

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro para verificar se é primo: "))
if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

# 3. Cálculo da Média de uma Lista

def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0

numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [float(num) for num in numeros]
print(f"A média dos números é: {calcular_media(numeros)}")

# 4. Contador de Vogais em uma Palavra

def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in palavra if letra in vogais)

palavra = input("Digite uma palavra: ")
print(f"O número de vogais em '{palavra}' é: {contar_vogais(palavra)}")

# 5. Conversão de Temperatura

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = celsius_para_fahrenheit(celsius)
print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F")