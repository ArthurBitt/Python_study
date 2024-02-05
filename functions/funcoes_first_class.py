"""
High Order Functions 
são funções que chamam outras funções

First Class Functions
São funções tratadas como dados, que podem ser armazenadas em variáveis e reutilizadas
como argumento para outras funções.
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa_saudacao(funcao, *args):
    return funcao(*args)

print(executa_saudacao(saudacao,"Bom dia", "Arthur"))

