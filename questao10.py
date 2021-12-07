deposito = float(input("Informe o deposito inicial: "))
juros = float(input("Informe a taxa de juros da poupança: "));
cont = 1;
total = deposito;
while cont <= 12:
    print("Valor no mês %d°: " % cont);
    taxa = (total * juros/100);
    total = (taxa + total);
    print("%.2f" % total);
    cont+=1;
ganho = (total - deposito)
print("O ganho com juros no periodo %.2f" % ganho);