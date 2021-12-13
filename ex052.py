tot = 0
n = int(input('Informe um número: '))
for c in range(1, n+1):
    if n % c == 0:
        print(f'\033[33m{c}', end=' ')
        tot += 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível {tot} vezes')
if tot == 2:
    print(f'E por isso ele é PRIMO!')
else:
    print(f'E por isso ele NÃO É PRIMO!')

