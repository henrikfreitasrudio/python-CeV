from random import randint
print('=-' * 12)
print('Jogo PAR ou ÍMPAR')
print('Valores entre 0 e 10')
v = 0
while True:
    print('=-' * 12)
    jog_num = int(input('Informe sua jogada: '))
    print('-' * 25)
    pc = randint(0, 10)
    r = jog_num + pc
    tipo = ' '
    while tipo not in 'PI':  # garante que a entrada será PpIi
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jog_num} e o computador {pc}, total de {r}', end=' ')
    print('DEU PAR' if r % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if r % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Fim de jogo!')
            break
    elif tipo == 'I':
        if r % 3 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Fim de jogo!')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {v} vezes')
