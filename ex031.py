# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
# passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 de viagens mais longas.
distance = int(input('Qual a distância da viagem em Km ? '))
if distance <= 200:
    print('O valor total da viagem é de R${:.2f}.'.format(float(distance * 0.50)))
elif distance >= 500:
    print('O valor total da viagem é de R${:.2f}'.format(float(distance * 0.40)))
else:
    print('O valor total da viagem é de R${:.2f}.'.format(float(distance * 0.45)))
print('Tenha uma boa viagem !')
