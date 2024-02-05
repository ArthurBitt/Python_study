"""
split. separa pelos caracter 
especificado ou espaço em branco por default ["olha", "só,","que"]

strip. retira os espaços
"""
x = ''

frase = "Olha só, que coisa interessante"
lista_frase = frase.split()
print(lista_frase)


for i, caractere in enumerate(lista_frase):
    x += (caractere.strip())
print(x)


lista_frase = ",".join(lista_frase)
print(lista_frase)