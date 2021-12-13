n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos podem formar um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO!')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO!')
    else: #resume os vários testes que terim que ser feitos para o isósceles
        print('ISÓSCELES!')
else:
    print('Os segmentos não podem formar um triângulo.')
