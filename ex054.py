from datetime import date

maiores = []
menores = []
cnt = 0
for c in range(1, 8):
    cnt += 1
    year = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(cnt)))
    age = (date.today().year - year)
    if age <= 17:
        menores.append(age)
    else:
        maiores.append(age)
print('Ao todo tivemos {} pessoas menores de idade\n'
      'E também tivemos {} pessoas maiores de idade.'.format(len(menores), len(maiores)))
