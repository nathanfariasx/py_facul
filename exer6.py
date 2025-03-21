# 1. Armazenamento de Informações de um Produto

produto = ("Notebook", 3500.00, 10)
print(f"Produto: {produto[0]}\nPreço: R$ {produto[1]:.2f}\nQuantidade em estoque: {produto[2]}")

# 2. Operações Matemáticas com Números em uma Tupla

numeros = tuple(int(input(f"Digite o {i+1}º número: ")) for i in range(4))

print(f"O número 9 apareceu {numeros.count(9)} vez(es).")
if 3 in numeros:
    print(f"O número 3 apareceu na posição {numeros.index(3) + 1}.")
else:
    print("O número 3 não foi digitado.")
print("Números pares digitados:", end=" ")
for num in numeros:
    if num % 2 == 0:
        print(num, end=" ")

# 3. Listagem de Cores do Arco-Íris

cores = ("Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta")
pos = int(input("Digite um número de 1 a 7 para ver a cor correspondente: "))
if 1 <= pos <= 7:
    print(f"A cor correspondente é: {cores[pos - 1]}")
else:
    print("Número inválido! Digite entre 1 e 7.")

# 4. Nomes de Alunos e Notas

alunos = ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)

print("Nomes dos alunos:")
for i in range(0, len(alunos), 2):
    print(alunos[i])

print("\nNotas dos alunos:")
for i in range(1, len(alunos), 2):
    print(alunos[i])

# 5. Classificação de Times de Futebol

times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 
         'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza')

print("Os três primeiros colocados são:", times[:3])
print("Os três últimos colocados são:", times[-3:])
print("Times em ordem alfabética:", sorted(times))

time_procurado = input("Digite o nome de um time para saber a posição: ")
if time_procurado in times:
    print(f"O {time_procurado} está na posição {times.index(time_procurado) + 1}.")
else:
    print(f"O time {time_procurado} não está na lista.")