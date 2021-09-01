pesos = []
for c in range(1, 6):
    peso = float(input('Peso da primeira {} pessoa ? '.format(c)))
    pesos.append(peso)
pesos.sort()
print('O maior peso lido foi de {:.1f}Kg.\nO menor peso lido foi de {:.1f}.Kg.'.format(pesos[4], pesos[0]))

# segunda maneira caso nao saiba a quantidade de repetições ou a lista não puder ser modificada:
#
# pesos = []
# maior = 0
# menor = 0
# for c in range(1, 6):
#     peso = float(input('Peso da primeira {} pessoa ? '.format(c)))
#     pesos.append(peso)
#     if c == 1:
#          maior = peso
#          menor = peso
#     else:
#         if peso > maior:
#           maior = peso
#         if peso < menor:
#           menor = peso
# print('O maior peso lido foi de {:.1f}Kg.\nO menor peso lido foi de {:.1f}.Kg.'.format(maior, menor))
