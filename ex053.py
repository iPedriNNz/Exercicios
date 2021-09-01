frase = str(input('Digite um frase: ')).upper().strip()
fraseinv = (frase[::-1])
print('O inverso de {} é {}'.format(frase, fraseinv))
if frase == fraseinv:
    print('A frase digitada é um PALÍNDROMO.')
else:
    print('A frase digitada não é um PALÍNDROMO.')
