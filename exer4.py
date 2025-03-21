# 1. Soma dos Elementos de uma 

numeros = input("Digite uma lista de números inteiros separados por espaço: ").split()
numeros = [int(num) for num in numeros]
soma = sum(numeros)
print(f"A soma de todos os elementos da lista é: {soma}")

# 2. Encontrar o Maior e o Menor Número

numeros = input("Digite uma lista de números inteiros separados por espaço: ").split()
numeros = [int(num) for num in numeros]
maior = max(numeros)
menor = min(numeros)
print(f"O maior número da lista é: {maior}")
print(f"O menor número da lista é: {menor}")

# 3. Remover Duplicatas

numeros = input("Digite uma lista de números inteiros separados por espaço: ").split()
numeros = [int(num) for num in numeros]
sem_duplicatas = []
for num in numeros:
    if num not in sem_duplicatas:
        sem_duplicatas.append(num)
print(f"Lista sem duplicatas: {sem_duplicatas}")

# 4. Inverter a Lista

palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
palavras_invertidas = palavras[::-1]
print(f"Lista invertida: {palavras_invertidas}")

# 5. Contar Ocorrências de um Elemento

numeros = input("Digite uma lista de números inteiros separados por espaço: ").split()
numeros = [int(num) for num in numeros]
numero_procurado = int(input("Digite o número que deseja contar: "))
ocorrencias = numeros.count(numero_procurado)
print(f"O número {numero_procurado} aparece {ocorrencias} vez(es) na lista.")