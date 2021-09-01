# Faça um algoritimo que mostre um novo salario com 15% de acrescimo
s = float(input('Qual o seu salário atualmente ? '))
rs = s + (s * 15 / 100)
print('O valor do seu novo salário seria de R${:.2f}'.format(rs))
