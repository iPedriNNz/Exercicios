op = 's'
maior = menor = media = div = cont = 0
while op in 's':
    number = int(input('Digite um valor: '))
    cont += 1
    div += 1
    media += number
    if cont == 1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        if number < menor:
            menor = number
    op = str(input('Quer continuar ? [S/N] '.strip().upper()))
print('Você digitou {} números e a média entre eles foi {:.2f}\n'
      'O maior valor foi {} e o menor valor foi {}'.format(cont, media / div, maior, menor))
