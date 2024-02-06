'''
dicionarios são estruturas de pares chave:valor
as chaves nao repetem
dicionarios sao mutaveis
'''

pessoa = dict()

pessoa = {"nome": "Arthur", "sobrenome": "Bittencourt"}
print(pessoa['sobrenome'])

pessoa = dict(
    nome="Arthur",
    sobrenome="Dos Santos Bittencourt",
    idade=26,
    enderecos=[{"rua": "rua x"}, {"rua": "rua y"}],
)
