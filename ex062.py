primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA:'))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        cont += 1
        print(termo, end=' → ')
        termo += razao
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais ? '))
print('Fim do programa!')
