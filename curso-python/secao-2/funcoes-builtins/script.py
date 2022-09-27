num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if num1.endswith('-', 0, 1):
    num1 = int(num1)
elif num1.isnumeric():  # caso retorne True
    num1 = int(num1)
else:
    num1 = 0

if num2.endswith('-', 0, 1):
    num2 = int(num2)
elif num2.isdecimal():  # caso retorne True
    num2 = int(num2)
else:
    num2 = 0

print(num1 + num2)
