times = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Ceará SC', 'Chapecoense', 'Corinthians',
         'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras',
         'Bragantino', 'Santos', 'Sport Recife', 'São Paulo')
print(f'A lista de times do brasileirão:\n {times}')
print('=-' * 20)
print(f'Os cinco primeiros são:\n {times[0]}, {times[1]}, {times[2]}, {times[3]}, {times[4]}.')
print('=-' * 20)
print(f'Os quatro ultimos são:\n {times[-4]}, {times[-3]}, {times[-2]}, {times[-1]}.')
print('=-' * 20)
print(f'Times em ordem alfabética:\n {sorted(times)}')
print('=-' * 20)
print(f'A Chapecoense está no {times.index("Chapecoense") + 1}ª lugar.')
