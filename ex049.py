number = int(input('Me mostre um número e eu te mostro a tabuada dele: '))
for n in range(1, 11):
    print('{} x {:2} = {}'.format(number, n, number * n))
