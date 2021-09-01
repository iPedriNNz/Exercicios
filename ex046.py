from time import sleep

run = int(input('''Iniciar lançamento da nave SPACEX 0D47 Mars ?
[ 1 ] - SIM
[ 2 ] - NÃO
Lançar ? '''))
if run == 1:
    print('Iniciando lançamento em: ')
    for c in range(10, 0, -1):
        print(c)
        sleep(1)
    print('LANÇADO!!')
else:
    print('FIM!')
# playsound('foguete10s.mp3')
