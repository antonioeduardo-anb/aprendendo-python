# bloco de codigo reutilizavel que executa ações especificas, ajuda a não fazer repetições de codigo

# função é definida com "def" tem um identificador "saudar" e variaveis que são chamadas de parametros "nome" "idade"
def saudar(nome, idade):
    print(f"olá {nome}, voce tem {idade} anos")

# executando a função e passando os arguemntos "Antonio" "37"
saudar("Antonio", "37")

# Parâmetro: variavel definida na criação da função (ex: nome, idade)
# Argumento: Valor real passado na chamada (ex: "Antonio", 36)

# usando valores padrão nos parametros, valores padrão devem ser colocados por ultimo
def conexao(ip, porta=8080):
    print(f"CONECTANDO NO IP {ip} NA PORTA {porta}")

conexao("192.168.0.0.1")# usa a porta 8080 por padrão

# uma função pode retornar um valor
def calcular_area_circulo(raio):
    return 3.1415 * (raio ** 2)

area = calcular_area_circulo(5)
print(f"Área: {area:.2f}") # Exibindo com 2 casas decimais

# usando Docstrings para explicar o funcionamento da função
def soma(x ,y):
    """soma dois numeros e retorna o resultado"""
    return x + y

# uma função deve fazer uma coisa bem definida, se uma função estiver fazendo varias coisas ela deve ser dividida

# usando args, *args é uma tupla que empacota todos os valores passados para a função
def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicar = multiplica(10, 50, 80, 90)# é possivel passar quantos valores quiser 
print(multiplicar)

# passando uma tupla como argumento
numeros = 12, 24, 29
multiplicar2 = multiplica(*numeros) # * desempacota a tupla antes de chamar a função 
# dependendo de onde o * é usado ele pode empacotar e desempacotar valores.