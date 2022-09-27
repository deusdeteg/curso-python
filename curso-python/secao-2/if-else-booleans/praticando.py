pergunta = ''

while pergunta != 'y':
    print('----------------------------------')
    idade = int(input('Qual a sua idade? '))
    
    if idade <= 10:
        print('voce e uma crianca')
    elif idade > 10 and idade < 18:
        print('voce e um adolencente')
    elif idade >= 18 and idade < 60:
        print('voce e um adulto')
    else:
        print('voce e um idoso')

    pergunta = input('deseja sair? (y/n) ')
    if pergunta == 'n':
        continue
    elif pergunta == 'y':
        break

