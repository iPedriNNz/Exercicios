# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
# ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

student1 = input('Nome do primeiro aluno ')
student2 = input('Nome do segundo aluno ')
student3 = input('Nome do terceiro aluno ')
student4 = input('Nome do quarto aluno ')
lista = [student1, student2, student3, student4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
