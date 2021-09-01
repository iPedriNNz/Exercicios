# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

student1 = input('Digite o nome do primeiro estudante: ')
student2 = input('Digite o nome do segundo estudante: ')
student3 = input('Digite o nome do terceiro estudante: ')
student4 = input('Digite o nome do quarto estudante: ')
lista_de_alunos = [student1, student2, student3, student4]
shuffle(lista_de_alunos)
print('A ordem de apresentação sera: {}'.format(lista_de_alunos))
