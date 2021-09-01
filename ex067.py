while True:
    print('-' * 20)
    print('[Digite um número negativo para finalizar o programa]')
    num = int(input('Quer ver a tabuada de qual valor ? '))
    print('-' * 20)
    if num < 0:
        print('Fim do programa ! Obrigado e volte sempre !')
        break
    print(f'''
  {num} x 1  = {num * 1}  
  {num} x 2  = {num * 2}
  {num} x 3  = {num * 3}
  {num} x 4  = {num * 4}
  {num} x 5  = {num * 5}
  {num} x 6  = {num * 6}
  {num} x 7  = {num * 7}
  {num} x 8  = {num * 8}
  {num} x 9  = {num * 9}
  {num} x 10 = {num * 10}''')
