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