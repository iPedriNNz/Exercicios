# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
# forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for n in range(1, 7):
    number = int(input('Digite o {} valor: '.format(n)))
    if number % 2 == 0:
        soma += number
        cont += 1
print('Você digitou {} números pares. A soma deles é {}'.format(cont, soma))
