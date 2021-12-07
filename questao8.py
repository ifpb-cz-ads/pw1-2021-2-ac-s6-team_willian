num1 = int(input("Insira um numero: "))
num2 = int(input("Insira outro numero pra ser divisivel por esse numero: "))
cont = 0;
total = num1;
while total >= num2:
    total = total - num2;
    cont = cont + 1;
print("O resultado da divisão é: ",cont);
print("O resto da divisão é", total);