# Escreva um programa que converta metros em cm e mm
mt = float(input('Quantos metros você gostaria de converter ? '))
cm = mt * 100
mm = mt * 1000
print('Em {} metros temos {:.0f} centimentros e {:.0f} milímetros.'.format(mt, cm, mm))
# Voce tambem pode fazer print('Em {} metros temos {:.0f} centimentros e {:.0f}
# milímetros.'.format(mt, mt * 100, mt * 1000)) assim nao precisa criar mais variáveis.
