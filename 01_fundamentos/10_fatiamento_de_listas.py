# Fatiamento
# índices:  0    1    2    3    4
letras = ["A", "B", "C", "D", "E"]


# [início:fim]
partes = letras[1:4]  # do índice 1 ao 3 (fim não incluído)

print(partes)


# Omitindo início ou fim
inicio = letras[:3]  # do início ao índice 2
fim = letras[2:]     # do índice 2 ao final

print(inicio)
print(fim)


# Definindo um passo
saltando = letras[0:5:2]  # do índice 0 ao 4, pulando de 2 em 2

print(saltando)