print('=' * 20)
print('10 Termos de uma PA')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
ultimo = primeiro + (10 * razão)
for c in range(primeiro, ultimo, razão):
    print(c, end=' -> ')
print('ACABOU.')
