"""
 Uma função de fechamento (ou “closure”) em Python é uma função aninhada (uma função dentro de outra função) que se lembra e tem acesso às variáveis do escopo da função externa, mesmo depois que a função externa terminou de ser executada1.

"""
   


def saudacao(msg):
    def nome(nome):
        return f'{msg}, {nome}!'
    
    return nome

saudacaoBomdia = saudacao("Bom dia") # argumento func externa pré definido 

print(saudacaoBomdia("Arthur")) # a variável que guarda o espaço da memória da função saudacao que gera a func nome, recebe um parâmetro. 