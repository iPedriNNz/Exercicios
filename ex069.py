homens = maioridade = mulheres20 = 0
while True:
    sexo = ' '
    op = ' '
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M] ')).strip().upper()
    print('-' * 20)
    while op not in 'SN':
        op = str(input('Quer continuar [S/N] ? ')).strip().upper()
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    if op == 'N':
        break
print(f'''
Total de pessoas com mais de 18 anos: {maioridade}
Ao todo temos {homens} homens cadastrados
E temos {mulheres20} mulheres com menos de 20 anos''')
