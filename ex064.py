#  Soma com flag de pausa
c = soma = 0
n = int(input(f'Informe um número: [999 para parar] '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Informe um número: [999 para parar] '))
print(f'Você digitou {c} números e soma entre eles é {soma}.')
