#12) Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
# Pergunte também o valor mensal que será pago.
# Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
inicial = float(input('Digite o valor inicial da divida:'))
juromensal = float(input('Digite o juro mensal: '))
valormpago = float(input(('Digite o valor mensal que sera pago: ')))
jurofinal = (valormpago * juromensal)
valortotal = (valormpago + jurofinal)
mesestotal = (inicial/valortotal)
print('Serão necessarios %.0f meses' % mesestotal)


