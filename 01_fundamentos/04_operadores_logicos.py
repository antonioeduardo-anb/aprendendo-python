"""
OPERADORES LÓGICOS

and → True somente quando todas as condições são True
or  → True quando pelo menos uma condição é True
not → inverte o valor lógico

Parênteses podem ser usados para definir a ordem de avaliação.
"""

ingresso = True
documento = True

if ingresso and documento:
    print("Entrada permitida 🍿")


estudante = False
idoso = True

if estudante or idoso:
    print("Desconto aplicado 💸")


chovendo = False

if not chovendo:
    print("Indo treinar 💪")


tem_dinheiro = True
feriado = False
fds = True

if tem_dinheiro and (feriado or fds):
    print("Partiu viagem! ✈️")

# Em Python, outros tipos de valores também podem ser avaliados
# como True ou False em uma condição.

bool("Eduardo")  # True
bool("")         # False

bool([1, 2, 3])  # True
bool([])         # False