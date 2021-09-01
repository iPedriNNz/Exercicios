numeros = [[], []]
numtemp = 0
for n in range(1, 8):
    numtemp = (int(input(f'Digite o {n}º número: ')))
    if numtemp % 2 == 0:
        numeros[0].append(numtemp)
    else:
        numeros[1].append(numtemp)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares em órdem crescente são:')
print(numeros[0])
print(f'Os números imapres em órdem crescente são:')
print(numeros[1])
