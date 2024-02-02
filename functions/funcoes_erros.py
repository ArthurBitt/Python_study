

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

x = 3

def scope():
    def other_func():
        y = 2
        print(x, y) 

    other_func()
    
    print(x)
    

# other_func() -  é chamada dentro func scope() apenas
scope()