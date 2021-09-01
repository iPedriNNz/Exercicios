al = float(input('Qual o altura da parede ? '))
la = float(input('Qual a largura da parede ? '))
ar = al * la
tn = float(ar / 2)
print('A área total de sua parede é {:.3f} metros². \nPara pinta-la serão necessários {} litros '
      'de tinta.'.format(ar, tn))
