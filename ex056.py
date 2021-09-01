midade = 0
homem = 0
nomehomem = ''
mulher20 = 0
for c in range(1, 5):
    print('{}ª Pessoa'.format(c))
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).upper().strip()
    midade = (midade + idade)
    if c == 1 and sexo in 'mM':
        nomehomem = nome
        homem = idade
    if sexo in 'mM' and idade > homem:
        homem = idade
        nomehomem = nome
    if sexo in 'fF' and idade <= 20:
        mulher20 = + 1
print('A média de idade do grupo é de {}'.format(midade / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(homem, nomehomem))
print('{} mulheres tem menos de 20 anos'.format(mulher20))
