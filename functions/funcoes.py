""" 
Funções
Uma função sem return por padrão retorna None - 
Podem receber argumentos - 
Replicam determinanda ação -
Uma função que retorna algum valor pode ser armazenada em uma variável
"""


def nome_func():
    print("function sem retorno e sem argumentos")


print(nome_func, "local da memória que guarda a func", sep="")
nome_func()


def nome_func(a, b, c):
    print("function com argumentos e sem retorno")


nome_func(1, 2, 3)


def nome_func():
    return "function com retorno, mas sem argumentos"


print(nome_func())
# funções com retorno devem ser exibidas ou armazenadas em variaveis


def nome_func(a, b, c):
    print("funtion com argumentos e com retorno")
    return a, b, c


print(nome_func("c", "a", "b"))


x = nome_func(1, 2, 3)
print(x)

x = print("-")
print(
    x
)  # executa o print pq print() chamou a função print,mas não tem retorno de valor - portanto, None.
