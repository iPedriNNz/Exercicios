cont = soma = 0
while True:
    number = int(input('Digite um número [Digite um numero negativo para parar]: '))
    if number < 0:
        break
    else:
        cont += 1
        soma += number
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')
