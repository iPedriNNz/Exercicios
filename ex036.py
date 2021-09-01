# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder
# 30% do salário ou então o empréstimo será negado.
home = float(input('Qual o valor da casa: R$  '))
salary = float(input('Qual o seu salário: R$ '))
months = int(input('Em quantos anos você gostaria de pagar ? ')) * 12
portion = home / months
if portion <= (salary / 100) * 30:
    print('Para pegar um casa de R$ {} a prestação será de {:.2f} '
          '\nEmpréstimo APROVADO!'.format(home, portion))
else:
    print('Para pegar um casa de R$ {} a prestação será de {:.2f} '
          '\nEmpréstimo NEGADO!'.format(home, portion))
