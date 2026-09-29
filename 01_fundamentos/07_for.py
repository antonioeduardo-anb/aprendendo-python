# ESTRUTURA FOR (Para cada...) Ideal para percorrer sequências (iteráveis) como strings, listas e intervalos.

# percorrendo uma string
nome = "Eduardo"
# para cada letra in nome 
for letra in nome:
    print("Letra -> :", letra)

# percorrendo range
# range é uma função que gera um iteravel de numeros especificados
for i in range(1, 10):
    print("Numero: ", i)

# pulando o numero 3
for i in range(1, 10):
    if i == 3:
        print("pulando o numero 3")
        continue # pula esse item e continua o loop
    print("numero atual: ", i)

# percorrendo lista e encontrando item
frutas = ["laranja", "abacaxi", "morango", "uva", "cereja" ," manga"]

print("buscando a uva ...")
for fruta in frutas:
    if fruta == "uva":
        print(fruta, "encontrada, parando loop ....")
        break # sai do loop
    print("verificando fruta atual:", fruta)    