# Exercicio 01

num = input('Digite um número inteiro: ')

try:
    num = int(num)
    if num % 2 == 0:
        print(f'O {num} é um numero par')
    else:
        print(f'O {num} é um numero inpar')
except:
    print(f'O {num} não é um inteiro')

# Exercicio 02

hora = input("Que horas são? ")

try:
    if int(hora) < 12 > 0:
        print('Bom dia!')
    elif 12 < int(hora) < 18:
        print('Boa tarde!')
    else:
        print("Boa noite!")
except:
    print('Digite um horário válido')

# Exercicio 03

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é muito curto')
elif 5 <= len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')

