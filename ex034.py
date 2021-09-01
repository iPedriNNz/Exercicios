# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o
# valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%
salary = int(input('Qual é o salário do funcionário ? '))
if salary > 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}.'.format(float(salary), (float(salary * 1.10))))
if salary <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}.'.format(float(salary), (float(salary * 1.15))))
