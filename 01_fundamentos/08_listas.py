# Listas são Estruturas Mutáveis, Uma lista armazena múltiplos valores em uma única variável, mantendo a ordem dos elementos através de índices.

lista_de_frutas = ["Maçã", "Banana", "Uva", "Manga"]

# acesando um item da lista pelo indice
# Índices:   [0]      [1]      [2]      [3]
# Valores:  "Maçã"   "Banana"  "Uva"  "Manga"
print(f"Fruta na posição 0: {lista_de_frutas[0]}")

# fazendo o indice 1 parar de apontar para "Banana" e passar a apontar para "morango"
lista_de_frutas[1] = "Morango"
print(lista_de_frutas)

# listas de listas(matrizes)
matriz01 = [
    [1, 2], # linha 0
    [3, 4], # linha 1
    [5, 6]  # linha 2
]

# cada índice da lista externa acessa uma linha, e cada indice das listas internas são colunas
print(f"linha 0, coluna 0: {matriz01[0][0]}")
print(f"linha 0, coluna 1: {matriz01[0][1]}")

print(f"linha 1, coluna 0: {matriz01[1][0]}")
print(f"linha 1, coluna 1: {matriz01[1][1]}")

print(f"linha 2, coluna 0: {matriz01[2][0]}")
print(f"linha 2, coluna 1: {matriz01[2][1]}")
