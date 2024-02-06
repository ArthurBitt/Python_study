import copy

pessoa = {"nome": "Arthur", "sobrenome": "Bittencourt"}

'''len - quantas chaves'''
print(pessoa.__len__())
print(len(pessoa))

'''keys'''
print(pessoa.keys())
for chave in pessoa.keys():
    print(chave)

'''values - iteravel com valores'''
print(pessoa.values())
for value in pessoa.values():
    print(value)

'''items traz par chave valor'''
print(pessoa.items())
for item in pessoa.items():
    print(item)

for i, chave_valor in enumerate(pessoa.items()):
    print(f'{i} - {chave_valor}')

'''setdefault - adiciona valor se a chave nao existe'''
pessoa.setdefault('lista',[1])
print(pessoa.items())

'''copy - retorna uma shallow copy'''
print(pessoa['lista']) # aqui pessoa tem lista [1]
pessoa_copy = pessoa.copy() # copia tudo que for imutável - mutaveis como list e dict são mantidas com a mesma ref na memoria
pessoa_copy['lista'][0] = 10000  # aqui a copia altera a lista mas a original acaba alterando tambe
print(pessoa['lista'])

pessoa_copy = copy.deepcopy(pessoa)
#aqui a copy tem as estruturas mutáveis desvinculadas da original
pessoa_copy['lista'][0] = 2
print(pessoa)
print(pessoa_copy)

'''get - obtem uma chave(chave[value])'''
print(pessoa.get('nome'))
print(pessoa.get('endereco')) # quando nao tem a chave

'''pop - apaga um item pela chave (del)'''

nome = pessoa.pop('nome')
print(nome)
print(pessoa)

'''popitem - apaga o ultimo item adicionado'''

ultima_chave = pessoa.popitem()
print(pessoa)

'''update - atualiza um dict com outro'''
pessoa.update({
    'nome': 'Arthur',
    
})

pessoa.update(idade = 26)