sexo = str(input('Qual o sexo da pessoa ? [M/F]')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Qual o sexo da pessoa ? [M/F]')).upper().strip()[0]
if sexo == 'M':
    print('Sexo masculino registrado com sucesso !')
else:
    print('Sexo feminino registrado com sucesso !')
print('FIM')
