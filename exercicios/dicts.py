
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

    for i,opcao in enumerate(pergunta.get('Opções')):
        print(f'{i}){opcao}')
    print()
    
    escolha = (input('Escolha uma opção: '))
    acertou = False
    escolha_int = None


    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >=0 and escolha_int < len(opcao):


        