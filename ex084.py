pessoas = list()
adicionar = list()
maior = menor = 0
while True:
    adicionar.append(str(input('Nome da pessoa: ').title()))
    adicionar.append(float(input('Peso da pessoa em Kg: ')))
    if len(pessoas) == 0:
        maior = menor = adicionar[1]
    else:
        if adicionar[1] > maior:
            maior = adicionar[1]
        if adicionar[1] < menor:
            menor = adicionar[1]
    pessoas.append(adicionar[:])
    adicionar.clear()
    op = str(input('Gostaria de continuar ? [S/N]')).upper()
    if op == 'N':
        break
print('=' * 60)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior:.2f}Kg, peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {menor:.2f}Kg, peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
