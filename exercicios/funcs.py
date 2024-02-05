"""
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

"""

def multiplicaTodosArgumentos(*args):
    
    lista_resultados = list()
    for i in args:
        lista_resultados.append(i*2)
    return lista_resultados

x = multiplicaTodosArgumentos(1,2,3,4,"a")

print(x)


def multiplicaTodosArgumentosNumericos(*args):
    lista_resultados = list()
    
    try:
        for i in args:   
            if  isinstance(i,str):    
                continue

            else:
                lista_resultados.append(i*2)      
    except:
        print(f"Valor {i} inválido")
        
         
    return f'Resultado: {sum(lista_resultados)}'


print(multiplicaTodosArgumentosNumericos(1,2,3))
print(multiplicaTodosArgumentosNumericos(1,2,"a"))



"""
# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
"""
def parOuImpar(*args):
    par = list()
    impar = list()
    
    for i in args:
        if  isinstance(i,str):    
                continue
        else:
            if i%2 == 0:
                par.append(i)
            else:
                impar.append(i)
    
    return par, impar

pares, impares = parOuImpar(1, 2, 3, 4, 5, 6, 7, 8, 9)

print("Números pares:", pares)
print("Números ímpares:", impares)




