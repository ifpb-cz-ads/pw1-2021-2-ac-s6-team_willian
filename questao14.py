codigo = -1
total = 0
while (codigo != 0):
    codigo = int(input('Digite o codigo comprado:'))
    quantidade = float(input('Digite a quantidade comprada: '))
    if codigo == 1:
        cont = (quantidade * 0.5)
        total = total + cont
    elif codigo == 2:
        cont = (quantidade * 1)
        total = total + cont
    elif codigo == 3:
        cont = (quantidade * 4)
        total = total + cont
    elif codigo == 5:
        cont = (quantidade * 7)
        total = total + cont
    elif codigo == 9:
        cont = (quantidade * 9)
        total = total + cont
    elif codigo == 0:
        print("Fim das compras")
    else:
        print('Código invalido')
print('O total das compras foi de %d' % total)
