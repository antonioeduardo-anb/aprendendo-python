"""
OPERADORES DE COMPARAÇÃO

Usados para comparar valores.
O resultado é sempre um booleano: True ou False.

==  igual
!=  diferente
>   maior
<   menor
>=  maior ou igual
<=  menor ou igual
"""


# Igualdade

admin_sistema = "master"
admin_digitado = input("Digite o admin: ")

if admin_digitado == admin_sistema:
    print("Acesso concedido ✅")
else:
    print("Usuário inválido ❌")


# Maior que

temp = float(input("Qual a sua temperatura?: "))

if temp > 37.0:
    print(f"Temperatura {temp}°C: Está com febre 🤒")
else:
    print(f"Temperatura {temp}°C: Tudo normal 😀")


# Maior ou igual

vagas_ocupadas = int(input("Total de pessoas agora: "))
LIMITE = 9

if vagas_ocupadas >= LIMITE:
    print("Capacidade máxima atingida! 🚫")
else:
    print(f"Pode entrar. Vagas restantes: {LIMITE - vagas_ocupadas}")