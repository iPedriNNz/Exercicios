def area(a, b):
    area = a * b
    print(f'A área do terreno de {a:}x{b} é de {area:.1f}m²')


print('CONTROLE DE TERRENOS')
largura = float(input('Largura (M): '))
altura = float(input('Altura (M): '))
area(largura, altura)
