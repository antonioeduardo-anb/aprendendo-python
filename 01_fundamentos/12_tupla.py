# tuplas são estruturas de dados imutaveis, uma vez criada ela não pode ser alterada, não possue append, remove ou atribuições por indices.

# sintaxe: pode ser criadas com ou sem parentases, a virgula é o que define
nomes = ("eduardo", "carlos", "joão")
cores = "azul", "verde", "amarelo" # Também é uma tupla!

# tupla de um unico item deve conter um , no final
tupla_real = ("valor",) 
apenas_str = ("valor") # errado: o python ve isso como uma string entre parenteses

# convertendo uma lista para uma tupla, util para "proteger" os dados da lista
lista_frutas = ["maçã", "pera", "banana", "uva"]
tupla_frutas = tuple(lista_frutas)

# motivos para usar tuplas:
# - Segurança: Garante que os dados não serão alterados por erro.
# - Performance: São levemente mais rápidas que listas.
# - Uso como Chaves: Podem ser usadas como chaves em dicionários (listas não).
