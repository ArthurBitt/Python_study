""" 
Funções
por padrão retornam None
Podem receber argumentos
Replicam determinanda ação
"""

def nome_func():
    print("function sem retorno e sem argumentos")

print(nome_func,"local da memória que guarda a func", sep="")
nome_func()

def nome_func(a, b, c):
    print("function com argumentos e sem retorno")

nome_func(1,2,3) 


def nome_func(): 
    return 'function com retorno, mas sem argumentos'

print(nome_func())
# funções com retorno devem ser exibidas ou armazenadas em variaveis

def nome_func(a,b,c): 
    print("funtion com argumentos e com retorno")
    return a,b,c

print(nome_func("c","a","b")) 




