tot = mais_mil = cont = valor_lower = 0
name_lower = ' '
print('=' * 25)
print('Bem-Vindo a Loja FREITAS')
print('=' * 25)
while True:
    nome = str(input('Produto: ')).strip()
    valor = float(input('Valor: R$ '))
    cont += 1
    if cont == 1 or valor < valor_lower:
        name_lower = nome
        valor_lower = valor
    if valor > 1000:
        mais_mil += 1
    tot += valor
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    print('-' * 25)
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total gasto nas compras foi de R${tot:.2f}')
print(f'Ao todo, {mais_mil} produtos custaram mais de R$1000,00')
print(f'O nome do produto mais barato é {name_lower} e custa {valor_lower} reais.')
