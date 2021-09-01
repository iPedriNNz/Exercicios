number = cont = soma = 0
number = int(input('Digite um número[999 para parar]: '))
while number != 999:
    cont += 1
    soma += number
    number = int(input('Digite um número[999 para parar]: '))
print(f'Voce digitou {cont} numeros e a soma entre eles foi {soma}! ')
