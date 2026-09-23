# Em Python, os valores que manipulamos são objetos.
#
# Uma variável é um nome associado a um objeto.
#
# Exemplo:

nome = "Eduardo"

# "Eduardo" é um objeto do tipo str.
# A variável "nome" é o nome que usamos para acessar esse objeto.
#
# Podemos imaginar:
#
#     nome ─────→ objeto "Eduardo"
#                  tipo: str
#
#
# Os objetos possuem características e comportamentos.
# Essas características e comportamentos podem ser acessados através
# de atributos e métodos usando o operador ponto (.).


nome.upper()

# .upper() é um método do objeto str.
# Ele transforma o texto para letras maiúsculas.


# Outro exemplo:

idade = 25

# 25 é um objeto do tipo int.
#
# Cada tipo de objeto possui seus próprios atributos e métodos.
# Por isso, operações disponíveis para um tipo podem não existir em outro.


# Isso também explica a tipagem dinâmica do Python:
#
# a variável não possui um tipo fixo; ela pode ser associada a objetos
# de tipos diferentes.

valor = 10        # valor → objeto int
valor = "Eduardo" # valor → objeto str


# Portanto, podemos pensar em Python desta forma:
#
# variável → objeto → tipo → atributos e métodos