# Programa que tire a média de duas notas de aluno e mostre a média
n1 = float(input('Qual o valor da primeira nota ? '))
n2 = float(input('Qual o valor da segunda nota ? '))
rs = n1 + n2
rz = float(rs / 2)
print('O valor total das notas do aluno é de {}.'.format(rs))
print('A média de notas do aluno é de {:.1f} '.format(rz))
