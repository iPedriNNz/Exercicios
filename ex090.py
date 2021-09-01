def linha():
    print('=' * 20)


alunos = dict()
alunos['nome'] = str(input('Nome do aluno: '))
alunos['média'] = float(input(f'Média de {alunos["nome"]}: '))
linha()
if alunos['média'] >= 7:
    alunos['situação'] = 'Aprovado'
elif 5 <= alunos['média'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'
for k, v in alunos.items():
    print(f'-{k} é igual a {v}')
