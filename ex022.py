# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao #odo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
name = str(input('Digite seu nome completo: '))
print('Seu nome com as letras minúsculas ficaria assim : {}'
      '\nCom as letras maiúsculas ficaria assim: {}'.format(name.lower(), name.upper()))

print('Ao todo seu nome tem {} letras.'.format(len(name.replace(' ', ''))))

namel = name.split()
print('O seu primeiro nome tem {} letras.'.format(len(namel[0])))
