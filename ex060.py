# Cálculo do fatorial de qualquer número
n = int(input('Informe um número: '))
c = n
fat = 1
print(f'O fatorial de {n} é: ')
while c > 0:
    fat *= c
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(fat)
