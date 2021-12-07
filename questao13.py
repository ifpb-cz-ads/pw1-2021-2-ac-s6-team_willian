total = 0
cont = -1
number = 1;
#O -1 do number é pra descontar o zero ao ser digitado.
while (number != 0):
    number = int(input('Digite um numero:'))
    cont = cont + 1
    total = (number + total);

print("Foram digitados %d numero(s) e a soma total desses números é de %d" %( cont, total));