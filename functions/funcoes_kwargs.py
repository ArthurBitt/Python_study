'''
Por padrão kwargs retorna um dicionário
Argumentos nomeados

desempacotamento (*, ** - nomeados(dicts))
'''

lista = [1,2]
dict_ = {"nome": "João",
        "sobrenome": "Gandolfo"}


def kwargs(*args, **kwargs):

    print("NÃO NOMEADOS: ", args)
    print()
    print("NOMEADOS")
    for chave, valor in kwargs.items():
        print(chave, valor)


# kwargs(1,3,4,"a", nome="Arthur", sobrenome ="Bittencourt")
kwargs(*lista, **dict_)