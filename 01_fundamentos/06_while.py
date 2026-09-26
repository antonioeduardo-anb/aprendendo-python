"""
WHILE

while é uma estrutura de repetição (loop).
Ele pode ser visto como um "if teimoso":
verifica a condição e executa o bloco repetidamente
enquanto ela for verdadeira.
"""


# LOOP COM CONTADOR

contador = 1

while contador <= 5:
    print(f"Repetição nº {contador}")

    # Atalho para:
    # contador = contador + 1
    contador += 1


# LOOP INFINITO
#
# É importante garantir que alguma coisa dentro do loop
# possa fazer a condição se tornar falsa.
#
# Caso contrário, o loop continuará executando indefinidamente.
#
# while True:
#     print("Isso nunca termina!")


# VALIDAÇÃO DE ENTRADA
#
# Aqui não sabemos quantas tentativas serão necessárias.
# O loop continua até o usuário fornecer a senha correta.

SENHA_MESTRE = "1234"
tentativa = ""

while tentativa != SENHA_MESTRE:
    tentativa = input("Digite a senha para acessar o sistema: ")

    if tentativa != SENHA_MESTRE:
        print("Senha incorreta! Tente novamente. ❌")

print("Acesso concedido! Bem-vindo. ✅")


# while é muito útil quando não sabemos antecipadamente
# quantas vezes o bloco precisará ser executado.
#
# Um exemplo comum é validar uma entrada até que ela seja válida.

