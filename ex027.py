# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente.
# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.
name = str(input('Digite seu nome: ')).title().strip().split()
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(name[0]))
print('Seu segundo nome é {}'.format(name[-1]))
