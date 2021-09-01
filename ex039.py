# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

year = int(input('Qual o ano do seu nasciemnto ? '))
age = date.today().year - year

print('Quem nasceu em {} tem {} em {}.'.format(year, age, date.today().year))
if age < 18:
    print('Ainda faltam {} anos para o alistamento'
          '\nSeu alistamento será em {}'.format(18 - age, year + 18))
elif age > 18:
    print('Você já deveria ter se alistado há {} anos.'
          '\nSeu alistamento foi em {}.'.format(age - 18, year + 18))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
