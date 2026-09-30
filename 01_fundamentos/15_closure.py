# Closure é quando uma função interna continua tendo acesso às variáveis da função externa, mesmo depois que a função externa terminou.

def fazer_saudacao(msg):

    def saudar(nome):
        # msg não foi definido aqui, mas saudar vai manter o acesso a ela mesmo depois que fazer_saudação foi finalizada
        return f"{msg} {nome}"
        
    # retornando a saudar sem executar, ela leva com sigo "msg"
    return saudar

    
falar_bom_dia = fazer_saudacao("Bom dia ")
falar_boa_tarde = fazer_saudacao("Boa Tarde ")
falar_boa_noite = fazer_saudacao("Boa Noite ")

# Mesmo que 'fazer_saudacao' já tenha terminado de executar, as funções abaixo ainda sabem o valor de 'msg'.
print(falar_bom_dia("Antonio"))
print(falar_boa_tarde("Carlos"))
print(falar_boa_noite("Miguel"))

# fazendo uma fabrica de saudações :)
nomes = ["Eduardo", "Jessica", "Fabio", "Rodrigo", "Cassio"]

for nome in nomes:
    print(falar_bom_dia(nome))
    print(falar_boa_tarde(nome))
    print(falar_boa_noite(nome))