# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
speed = float(input('Qual a velocidade do carro ? '))
if speed <= 80.0:
    print('Tenha um bom dia e dirija com cuidado !')
else:
    print('MULTADO! Você excedeu o limite que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format((speed - 80) * 7))
    print('Tenha um bom dia e dirija com cuidado !')
