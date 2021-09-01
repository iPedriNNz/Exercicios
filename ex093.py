jogador = dict()
gols = list()
jogador['nome'] = str(input('Qual o nome do jogador ? '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
for g in range(0, partidas):
    gols.append(int(input(f'Quantos gols ele fez na {g + 1}ª partida ? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-' * 40)
print(jogador)
print('-' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-' * 40)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'   =>  Na {i + 1} partida ele fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
