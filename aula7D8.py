# Faça um algoritimo que calcule 5% de desconto
n1 = float(input('Qual o valor original do produto ? '))
pc = float(n1 * 0.05)
rs = float(n1 - pc)
print('O valor do produto com desconto seria de R${:.2f}'.format(rs))
# Podendo tambem ser feito da seguinte forma
# preço = float(input('Qual o valor original do produto ? '))
# novo = preço - (preço * 5 / 100)
