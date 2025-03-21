# 1. Cadastro de Alunos

alunos = {}
while len(alunos) < 3:
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

print("\nLista de alunos e suas notas:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota}")
# 2. Contagem de Caracteres em uma Palavra

palavra = input("Digite uma palavra: ")
contagem = {}

for letra in palavra:
    contagem[letra] = contagem.get(letra, 0) + 1

print("Contagem de caracteres:", contagem)
# 3. Dicionário de Tradução

traducao = {
    "casa": "house",
    "gato": "cat",
    "cachorro": "dog",
    "livro": "book",
    "carro": "car"
}

palavra = input("Digite uma palavra em português: ").lower()
if palavra in traducao:
    print(f"A tradução de '{palavra}' é '{traducao[palavra]}'.")
else:
    print("Tradução não encontrada.")
# 4. Estatísticas de um Texto

frase = input("Digite uma frase: ").lower()
palavras = frase.split()
contagem_palavras = {}

for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

print("Contagem de palavras:", contagem_palavras)
# 5. Catálogo de Produtos

catalogo = {
    101: ("Notebook", 3500.00),
    102: ("Mouse", 80.00),
    103: ("Teclado", 150.00),
    104: ("Monitor", 900.00),
    105: ("Impressora", 1200.00)
}

codigo = int(input("Digite o código do produto: "))
if codigo in catalogo:
    produto, preco = catalogo[codigo]
    print(f"Produto: {produto}, Preço: R$ {preco:.2f}")
else:
    print("Produto não encontrado.")
