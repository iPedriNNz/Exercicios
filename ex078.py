num = []
cont = 0
for v in range(0, 5):
    cont += 1
    num.append(int(input(f'Digite um número para o posição {cont}: ')))
maior = max(num)
menor = min(num)
print(f'Você digitou os números {num}')
print(f'O maior número digitado foi {maior} e ele apareceu na {num.index(maior) + 1}ª posição')
print(f'O maior número digitado foi {menor} e ele apareceu na {num.index(menor) + 1}ª posição')
