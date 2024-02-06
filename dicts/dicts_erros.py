'''Keyerror - acontece quando é requisitado um valor para uma chave que nao existe
dict[key] - key não existe
'''

pessoa = dict(nome='arthur',sobrenome = 'bittencourt')

del pessoa['nome']
print(pessoa['nome'])

