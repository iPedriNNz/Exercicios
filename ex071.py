r1 = r10 = r20 = r50 = 0
print('=' * 60)
print('              CAIXA ECNÔMICA FEDERAL DAS ARABIA')
print('=' * 60)
valor = int(input('Qual valor você quer sacar ? R$'))
while valor >= 50:
    valor -= 50
    r50 += 1
while valor >= 20:
    valor -= 20
    r20 += 1
while valor >= 10:
    valor -= 10
    r10 += 1
while valor >= 1:
    valor -= 1
    r1 += 1
if r50 > 0:
    print(f'Total de {r50} notas de R$ 50,00 ')
if r20 > 0:
    print(f'Total de {r20} notas de R$ 20,00 ')
if r10 > 0:
    print(f'Total de {r10} notas de R$ 10,00 ')
if r1 > 0:
    print(f'Total de {r1} notas de R$ 1,00 ')
print('=' * 60)
print('Volte sempre a CAIXA ECNÔMICA FEDERAL DAS ARABIA! Tenha um bom dia !')
