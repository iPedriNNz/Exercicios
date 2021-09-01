time = list()
jogador = dict()
gols = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual o nome do jogador ? '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    gols.clear()
    for g in range(0, partidas):
        gols.append(int(input(f'Quantos gols ele fez na {g + 1}ª partida ? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('Responda S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador ? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca} !')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i + 1}fez {g} gols')
    print('-=' * 30)
print('<<VOTLE SEMPRE>>')
