# Crie algoritimo que leia e mostre o dobro, triplo e raiz quadrada
n1 = int(input('Digite um número'))
db = n1 * 2
tp = n1 * 3
rz = pow(n1, 1 / 2)
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {}'.format(n1, db, tp, rz))
