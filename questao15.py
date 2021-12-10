#15) Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
 # Imprima a tabuada da operação escolhida. Repita até que a opção "saída" seja escolhida.
option = -1
number_1 = int(input('Digite o primeiro numero: '))
number_2 = int(input('Digite o segundo numero: '))
print('===MENU===')
while(option != 0):
    option = int(input('DIGITE 1 PARA ADIÇÃO: \n DIGITE 2 PARA SUBTRAÇÃO \n DIGITE 3 PARA MULTIPLICAÇÃP \n DIGITE 4 PARA DIVISÃO \n DIGITE 0 PARA SAIR \n  '))

    if option == 1:
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif option == 2:
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif option == 3:
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif option == 4:
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2);
