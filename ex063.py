print('Sequencia de Fibonacci')
nant = 1
Fibonacci = 0
n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))
while n != 0:
    print('{}'.format(Fibonacci), end=' → ')
    Fibonacci = Fibonacci + nant
    Nant = Fibonacci - nant
    n -= 1
print('FIM')
