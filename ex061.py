# Gerador de PA usando While
print('Gerador PA')
print('-=' * 10)
p = int(input('Primeiro termo da uma PA: '))
r = int(input('Razão: '))
cont = 0
termo = p
while cont < 10:
    print(termo, end=' -> ')
    termo += r
    cont += 1
print('FIM.')
