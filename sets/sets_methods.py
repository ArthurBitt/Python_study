# cria set vazio
s1 = set()

#add adiciona valor no set
s1.add(1)
s1.add("Arthur")
print(s1)
#update atualiza, de forma iterada o set - fragmentado

s1.update("Ola")
s1.update(('Bittencourt',2)) # empacota em uma tupla
print(s1)

# discard elimina valor
s1.discard("Bittencourt")
print(s1)

# clear - limpa o set
s1.clear()
print(s1)