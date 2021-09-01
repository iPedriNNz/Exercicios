numeros = (
'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
'Quatorze', 'Quinze', 'Dezesseis',
'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        number = int(input('Digite um número entre 0 e 20: '))
        if 0 <= number <= 20:
            break
        print('Tente novamente. ', end=' ')
    print(f'Você digitou o número {numeros[number]}')
    op = str(input('Quer continuar [S/N] ')).upper().strip()
    if op == 'N':
        break
print('Volte sempre !')
