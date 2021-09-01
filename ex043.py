# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
# Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
weight = float(input('Informe seu peso (Kg) '))
height = float(input('Informe sua altura (metro e cm '))
imc = weight / (height * height)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Cuidado você está na faixa de peso ABAIXO DO PESO.')
elif 18.5 <= imc <= 25:
    print('PARABÉNS você está na faixa de peso IDEAL.')
elif 25 <= imc <= 30:
    print('Cuidado você está na faixa de peso SOBREPESO')
elif 30 <= imc <= 40:
    print('Cuidado você está na faixa de peso OBSIDADE')
else:
    print('Cuidado você está na faixa de peso OBESIDADE MÓRBIDA')
