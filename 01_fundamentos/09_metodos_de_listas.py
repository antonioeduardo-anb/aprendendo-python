# metodos de listas são funções internas para manipular a estrutura e os dados das listas

nomes = ["Antonio", "Carlos", "Eduardo", "Gabriel", "Marcelo"]
#ADIÇÕES:
# append, adiciona um item no final da lista original
nomes.append("Beatriz")

# insert, adiciona um item em um indice "empurrando" o resto
nomes.insert(1, "Davi")

# print da lista depois das adições
print(nomes)

#REMOÇÕES:
# pop, remove por indice e retorna o item 
item_removido = nomes.pop(1)

# remove, remove a primeira ocorrencia do valor literal
nomes.remove("Gabriel")

# lista nomes depois das remoções
print(f"nome removido com pop: {item_removido}")
print(nomes)

# ORGANIZAÇÂO:
numeros = [5, 2, 3, 9, 8, 4, 1, 6, 7]

# sort. ordena a lista original
numeros.sort()
print(numeros)

# index, busca a posição de um elemento 
posicao_do_cinco = numeros.index(5)
print(f"o cinco está no index: {posicao_do_cinco}")

# len(), função global que conta quantos itens existem
tamanho = len(numeros)
print(f"a lista tem {tamanho} itens")

# LIMPEZA
# clear(), esvazia a lista
nomes.clear()
print(f"lista vazia ... {numeros}")