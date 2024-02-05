"""

try: tenta executar o código
except: ocorreu algum erro ao tentar executar

"""

numero_str = input("Vou dobrar o número que voce digitar: ")

try:
    print("STR:", numero_str)
    numero_float = float(numero_str)
    print("Dobro: ", numero_float * 2)

    if numero_str.isalpha():
        print("Isso não é um número")
except:
    print(f" O valor: {numero_str} não é possível ser calculado")
