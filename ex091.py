from operator import itemgetter
from random import randint
from time import sleep

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('=' * 30)
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('=' * 30)
print('Ranking dos jogadores')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar | {v[0]} com {v[1]}.')
    sleep(1)
