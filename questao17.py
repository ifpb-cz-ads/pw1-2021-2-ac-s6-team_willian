#17) Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

start = 2
end =int(input('Digite um numero:'))

for i in range(start, end+1):
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)
