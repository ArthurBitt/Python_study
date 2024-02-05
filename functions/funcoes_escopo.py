"""
Escopo é o local de atuação do código
pode ser local ou global 
local é restrito a um bloco, enquanto global é em todo código
A key word global transforma uma variável do escopo externo ser a mesma do escopo interno 
"""

"""escopo global"""
x = "Escopo Global"  # x do módulo


def scope():

    # global x # -> má prática alterar o global pelo escopo interno

    x = "Local Scope()"  # x da função scope

    def other_func():
        x = "Local other_func()"  # x da função other_func
        print(x)

    other_func()

    # x = " sobreescrevi o x local de scope() me apague e verá"

    print(x)


print(x)  # global
scope()  # chamada de scope()

# print(x , "- agora global") # aqui local scope vira global - após a chamada de scope.


""" se fosse atribuido global a x de other_func() seria ele e não o x de scope() a ser printado por último"""

x = 2  # definida depois da função  - não é utilizado
