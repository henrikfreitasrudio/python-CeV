soma = cont = maior = menor = 0
while True:
    n = float(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if r == 'n':
        break
print(f'Você digitou {cont} números. A média é {soma / cont:.2f}')
print(f'O maior é {maior} e o manor é {menor}. ')