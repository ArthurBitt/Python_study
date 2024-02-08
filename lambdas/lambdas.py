'''Introdução à função lambda (função anônima de uma linha)
A função lambda é uma função como qualquer
outra em Python. Porém, são funções anônimas
que contém apenas uma linha. Ou seja, tudo
deve ser contido dentro de uma única
expressão.

estrutura de uma lambda
lamda o parametro: o que será retornado, valores

'''


lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena():
    print(item)
    return item['nome']

lista.sort(key=lambda item: item['nome'])