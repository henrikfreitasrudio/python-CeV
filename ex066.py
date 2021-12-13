# soma com flag de parada
cont = soma = 0
while True:
    n1 = int(input('Informe um valor (999 para parar): '))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print(f'A soma dos {cont} números é {soma}.')
