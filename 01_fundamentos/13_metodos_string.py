# split, separa um astring em uma lista usando un caractere especificado para separar os itens

frase = "Olha só, que coisa interessante, esses metodos"
lista_frase = frase.split(",") # separa por ","
print(lista_frase)

# limitando o numero de divsões
site = "www.google.com"
site_dividido = site.split(".", 1) # só vai dividir no primeiro "." encontrado
print(site_dividido)

# join, join faz o contrario de split ele une uma lista em uma string
texto = ["Python", "é", "legal"]
str_texto = " ".join(texto) # unindo a lista e separando por espaço
print(str_texto)

# > uso interessante, criando um caminho de dirtetorio de uma lista
lista = ["home", "musicas", "lançamentos", "2026"]
diretorio = "/".join(lista)
print(diretorio)

# > tranformando uma string
fala = "eu gosto de programar"
# transformar em lista
fala_lista = fala.split()
#lista criada
print(fala_lista)
# modificando a lista
fala_lista[0] = "Nos"
fala_lista[1] = "gostamos"
# transformando de volta em string
fala = " ".join(fala_lista)
print(fala)

