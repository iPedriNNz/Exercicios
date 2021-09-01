total = cont1000 = 0
produtoba = ' '
valorba = 0
print('=' * 20)
print('LOJA SUPER BARATÃO')
print('=' * 20)
while True:
    name = str(input('Nome do produto: ')).title()
    valor = float(input('Valor do produto: R$ '))
    total += valor
    if valor >= 1000:
        cont1000 += 1
    if valorba == 0 or valorba > valor:
        valorba = valor
        produtoba = name
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar ? [S/N]')).upper().strip()
    if op == 'N':
        break
print('-' * 20)
print('FIM DO PROGRAMA')
print('-' * 20)
print(f'''
O total da compra foi R$ {total:.2f}
Temos {cont1000} produtos custando mais de R$ 1000.00
O produto mais barato foi {produtoba} que custa R$ {valorba:.2f}
Obrigado e volte sempre !''')
