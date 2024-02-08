
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

questions = list()
resps = list()

for pergunta in perguntas:
    print(pergunta.get('Pergunta'))
    print()

    opcoes = pergunta.get('Opções')

    for i,opcao in enumerate(opcoes):
        print(f'{i+1}){opcao}')
    print()
    
    escolha = (input('Escolha uma opção: '))

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    qtd_acertos = 0


    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >=0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
                qtd_acertos +=1
            
    
    if acertou:
        print()
        print("Acertou")
    else:
        print("Errou")

print(f"Voce acertou {qtd_acertos} pergunta de {len(perguntas)}")