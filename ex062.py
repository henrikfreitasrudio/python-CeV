# PA v3.0
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0
termo = p
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont < total:
        print(termo, end=' -> ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos deseja mostrar a mais? '))
print('FIM.')
print(f'Ao todo foram exibidos {total} termos da PA.')
