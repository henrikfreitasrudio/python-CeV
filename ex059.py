from time import sleep
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
op = 0
while op != 5:
    print('''O que deseja fazer?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    op = int(input('>>>>> Informe sua opção: '))
    if op == 1:
        print('SOMANDO:')
        print(f'{n1} + {n2} = {n1 + n2}')
    elif op == 2:
        print('MULTIPLICANDO:')
        print(f'{n1} X {n2} = {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print('O primeiro é maior!')
        else:
            print('O segundo é maior!')
    elif op == 4:
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    elif op == 5:
        print('FINALIZANDO...')
    else:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!!!')
    print('=-=' * 10)
sleep(2)
print('Fim do programa! Volte sempre')
