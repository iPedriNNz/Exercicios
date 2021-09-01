# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS GUANABARA '))
value = float(input('Digite o valor das compras: R$ '))
pay = int(input('''Escolha uma forma de pagamento
[ 1 ] À vista no dinheiro
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão 
[ 4 ] 3x ou mais no cartão
Qual é a opção ? '''))
if pay == 1:
    print('À vista no dinheiro conseguimos um desconto de 10%,'
          'você irá pagar R$ {:.2f}'.format(value - (value / 100 * 10)))
elif pay == 2:
    print('À vista no cartão conseguimos um desconto de 5%,'
          'você irá pagar R$ {:.2f}'.format(value - (value / 100 * 5)))
elif pay == 3:
    print('Em até duas vezes no cartão não tem juros, portanto o valor se manteria o mesmo R$ {:.2f}'.format(value))
elif pay == 4:
    parcels = int(input('Informe o número de parcelas: '))
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.\n'
          'Sua compra de R$ {:.2f} irá custar R$ {:.2f} no final.'.format(parcels, (value / 100 * 20 + value) / parcels,
                                                                          value, (value / 100 * 20 + value)))
else:
    print('OPÇÃO INVALIDA ')
