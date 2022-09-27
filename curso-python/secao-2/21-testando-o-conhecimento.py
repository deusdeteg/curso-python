nome = input("Qula o seu nome: ")
idade = input("Qual sua idade: ")
altura = float(input("Qual a sua altura: "))
peso = float(input("Qual o seu peso: "))
imc = peso / altura ** 2
ano_atual = 2022
ano_nascimento = ano_atual - int(idade)

print(
    f"{nome} tem {idade} anos sua altura é {altura:.2f} e seu peso é {peso:.2f}. O IMC de {nome} é {imc:.2f} ele "
    f"nasceu no ano de {ano_nascimento}")
