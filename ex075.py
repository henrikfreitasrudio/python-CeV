cont = 0
valor = (int(input('Informe um número: ')), int(input('Informe outro número: ')), int(input('Informe mais um número: ')),
         int(input('Informe o último número: ')))
print('Os valores informados foram:', end=' ')
for c in valor:
    print(c, end=' ')
    if c == 3:
        cont += 1
print(f'\nO número 9 foi informado {valor.count(9)} vezes')
if cont == 1:
    print(f'O primeiro valor 3 apareceu na {(valor.index(3)) + 1}ª posição.')
else:
    print('O valor 3 não foi informado em nenhuma posição.')
# faltou a tupla com os números pares
 