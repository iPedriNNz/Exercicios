# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
note1 = float(input('Digite a primeira nota: '))
note2 = float(input('Digite a segunda notea: '))
average = (note1 + note2) / 2
print('Tirando {} e {} a sua média é {}'.format(note1, note2, average))
if average < 5.0:
    print('Sua média é de {} portanto você está REPROVADO!'.format(average))
elif 5.0 <= average <= 6.9:
    print('Sua média é de {} portanto você esta de RECUPERAÇÃO!'.format(average))
else:
    print('Sua média é de {} portanto você foi APROVADO'.format(average))
