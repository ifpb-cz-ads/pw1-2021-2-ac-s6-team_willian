#18) Escreva um programa que calcule o resto da divisão inteira entre dois números.
 #   Utilize apenas as operações de soma e subtração para calcular o resultado.

number1 =int(input('Digite o maior numero ex(25):'))
number2 = int(input('Digite o menor numero ex(3): '))
while(number2 <= number1):
    number1 = number1 - number2

print("O resto da divisao é: %d " % number1)
