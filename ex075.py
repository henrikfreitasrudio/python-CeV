valor = (int(input('Informe um número: ')),
         int(input('Informe outro número: ')),
         int(input('Informe mais um número: ')),
         int(input('Informe o último número: ')))
print(f'Os valores informados foram: {valor}')

print(f'O número 9 apareceu {valor.count(9)} vezes')
if 3 in valor:
    print(f'O primeiro valor 3 apareceu na {(valor.index(3)) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição!!')

print('Valores pares na tupla: ', end='')
for c in range(0, len(valor)):
    if valor[c] % 2 == 0:
        print(valor[c], end=' ')
