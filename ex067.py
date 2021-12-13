while True:
    n = int(input('Deseja ver a tabuada de qual número? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(0, 10):
        print(f'| {n} x {c} = {n*c} |')
    print('-' * 30)
print('Programa Tabuada Finalizado!!')
