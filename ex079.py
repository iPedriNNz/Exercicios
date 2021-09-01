num = []
while True:
    numadd = int(input('Digite um número para adicionar a lsita: '))
    if numadd not in num:
        num.append(numadd)
        print('Valor adicionado com sucesso...')
    else:
        print('Esse número ja existe na lista !')
    op = str(input('Gostaria de continuar ? [S/N]')).upper().strip()
    while op not in 'SN':
        print('Opção incorreta tente novamente')
        op = str(input('Gostaria de continuar ? [S/N]')).upper().strip()
    if op == 'N':
        break
print('=' * 80)
num.sort()
print(f'Os números digitados em ordem crescente foram: {num}', end='')
