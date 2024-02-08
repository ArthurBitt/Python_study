'''
set - conjuntos em python

aceitam apenas imutáveis como valor interno

mutáveis

não indexados, não ordenados e heterogeneos

'''


s1 = set('arthur')

s2 = {1,"Arthur",3.2, True}

print(s2)


'''iterando set'''

print(1 in s2)

# set não possui index

for valor in s2:
    print(valor)