#16) Escreva um programa que leia um número e verifique se é ou não um número primo.
#   Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido.
#  Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
number = int(input('Digite um numero:'))
cont = number;
div = 0;
while cont >= 1:
    if(number % cont == 0):
        div = div + 1
    cont = cont - 1
if(div == 2):
    print("O NUMERO É PRIMO")
else:
    print("O NUMERO NÃO É PRIMO")
