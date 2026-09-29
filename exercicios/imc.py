# imc = peso / (altura * altura)

nome =input("Digite seu nome > ")
altura = float(input("Digite sua altura > "))
peso = int(input("Digite seu peso > "))
imc = peso / (altura * altura)
print(nome, "tem", altura, "de altura.")
print("pesa", peso, "kilos e seu IMC é: ", imc)