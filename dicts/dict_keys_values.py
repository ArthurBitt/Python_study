pessoa = dict()

'''criando/alterando chave valor diretamente'''
pessoa['nome'] = "Arthur"
print(pessoa['nome'])
pessoa['nome'] = 'Lourenço'
print(pessoa['nome'])

'''criando chave dinamica'''
chave = 'nome'
pessoa[chave] = 'Lourenço'
print(pessoa['nome'])

'''Acessando chaves e valores'''
pessoa['sobrenome'] = 'Bittencourt'
print(pessoa['sobrenome'])


for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')

print("get: ", pessoa.get('sobrenome', None))

'''Deletando chaves e valores'''
print(pessoa)
del pessoa['sobrenome']
print(pessoa)
print("get: ", pessoa.get('sobrenome', None))

