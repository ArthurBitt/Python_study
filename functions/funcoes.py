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


# Especificações

"""argumentos Padrão"""
def nome_func(a, b = 1):
    # Definição da func - lógica
    soma = a + b 
    return soma

print(nome_func(1)) 
print(nome_func(1 + 2)) # b ainda pode receber um argumento

"""argumentos nomeados - valor declarado associado ao parametro"""
def nome_func(mat, fis, quim):
    return mat, quim, fis

print(nome_func(mat = 8, fis = 1, quim=11))

"""argumentos Posicionais - valor exibido conforme a ordem"""
def nome_func(a,b,c):
    return f'{a} - {b} - {c}'

print(nome_func(1,2,3))


""" argumento None """
def nome_func(a,b,c = None):
    if c is not None:
        print(f'a: {a}, b: {b}, c: {c}')
    else:
        print(f'a: {a}, b: {b}')
""""em verificações 0, 0.0,  são considerados False - None na verificação aceita is e is not - se o valor padrão de c fosse 0, 0.0, e essa verificação fosse feita, se o valor 0 fosse passado fora do default, o programa não exibiria o código do if, mas do else."""


#! Erros e Bugs

""" def nome_func(b = 1, a):  
    soma = a + b  
    return soma 
argumentos padrão devem vir antes dos nomeado - parameter without a default follows parameter with a default"""

def nome_func(a):
    return a

""" nome_func() - a func tem um parâmetro que deve ser preenchido, mas é chamada sem receber argumentos - missing required positional arguments"""

"""nome_func(1,2) - a func tem um parâmetro que deve ser preenchido, mas é chamada com mais de 1 argumento -  takes 1 positional argument but 2 were given"""

def nome_func(a):
    print(a, "retorna nada mas ainda sim é chamada com print")

"""print(nome_func()) - retorna a e None - a func não retorna nada, mas é printada - o print mostra o argumento e None - argumento e Valor padrão de retorno"""