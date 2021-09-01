# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot

co = float(input('Qual o comprimento do cateto oposto ?'))
ca = float(input('Qual o comprimento do cateto adjacente'))
qc = hypot(co, ca)
print('O comprimento da hipotenusa é de {:.2f}'.format(qc))
