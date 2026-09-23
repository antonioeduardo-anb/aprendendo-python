"""
input() = função usada para receber uma entrada do usuário.

Quando input() é executado, o programa pausa e espera o usuário
digitar algo e pressionar Enter.

O valor retornado por input() é sempre uma string (str).

if = estrutura condicional usada para executar um bloco de código
quando uma condição é verdadeira.

elif (else if) permite testar outra condição caso a anterior seja falsa.

else executa um bloco quando nenhuma das condições anteriores é verdadeira.
"""


# INPUT
# Tudo que vem de input() é uma string.
# Mesmo que o usuário digite um número, ele será recebido como texto.

idade = input("Qual é a sua idade? ")

# Se o usuário digitar 25:
#
# idade → "25"
# tipo  → str
#
# Por isso, isto causaria um erro:
#
# idade + 1
#
# porque estamos tentando somar uma string com um inteiro.


# CONVERSÃO DE TIPOS
# Podemos converter a string "25" para o inteiro 25 usando int().

idade = int(idade)

# Agora:
#
# idade → 25
# tipo  → int

idade_somada = idade + 1

print(idade_somada)


# IF / ELSE
# O bloco do if é executado somente se a condição for verdadeira.

if idade >= 18:
    print("maior de idade 🧔🏻")
else:
    print("menor de idade 🧒🏻")


# ELIF
# elif significa "senão, se".
# Ele permite testar outra condição caso a anterior seja falsa.

nota = int(input("Qual sua nota? "))

if nota >= 9:
    print("Excelente! 🏆")

elif nota >= 7:
    print("Você passou! ✅")

elif nota >= 5:
    print("Exame final... 📝")

else:
    print("Reprovado. ❌")

# O Python verifica as condições de cima para baixo.
# Quando encontra uma condição verdadeira, executa seu bloco
# e ignora os demais elif e o else.

# O else, quando utilizado, deve ser o último da estrutura.