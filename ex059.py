numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
op = 0
while (op != 5):
    print('=-' * 20)
    print('Escolha uma opção:')
    op = int(input('''    [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    >>>Qual a sua opção ? '''))
    if op == 1:
        print('A soma entre {} e {} é {}'.format(numero1, numero2, numero1 + numero2))
    elif op == 2:
        print('Na multiplicação {} x {} o produto é {}'.format(numero1, numero2, numero1 * numero2))
    elif op == 3:
        if numero1 > numero2:
            print('O número {} é o maior.'.format(numero1))
        elif numero2 > numero1:
            print('O número {} é o maior.'.format(numero2))
        else:
            print('Os dois números são iguais !')
    elif op == 4:
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('=-' * 20)
        print('Fim do programa.\nObrigado e volte sempre !!')
    else:
        print('Opção inválida tente novamente !')
