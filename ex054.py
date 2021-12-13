from datetime import date

maiorIdade = 0
menorIdade = 0
atual = date.today().year
for c in range(0, 7):
    ano = int(input(f'Em que ano nasceu a {c + 1}ª pessoa? '))
    if (atual - ano) <= 21:
        maiorIdade += 1
    else:
        menorIdade += 1
print(f'ANALISANDO OS DADOS...')

print(f'Ao todo temos: ')
print(f'{menorIdade} pessoas ainda não atingiram a maioridade.')
print(f'{maiorIdade} pessoas atingiram a maioridade.')
