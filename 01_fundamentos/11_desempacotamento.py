# UNPACKING (Desempacotamento)
# Extrai valores de um iterável diretamente para variáveis.


# Desempacotamento direto
# O número de variáveis deve corresponder ao número de valores.

nomes = ["Antonio", "Carlos", "Miguel"]

nome1, nome2, nome3 = nomes


# Usando * para capturar o restante
# * transforma os valores restantes em uma lista.

primeiro, *resto = ["Davi", "Rita", "Leandro", "Jose"]

# primeiro → "Davi"
# resto → ["Rita", "Leandro", "Jose"]


# Usando _ para ignorar valores
# _ indica um valor que não será utilizado.

n1, _, n3, *_ = ["Ana", "Beatriz", "Caio", "Duda", "Elaine"]

print(f"selecionados: {n1} e {n3}")