somaIdades = 0
somaMulher = 0
idadeMaisVelho = 0
nomeMaisVelho = ''
for c in range(0, 4):
    print(f'--------- {c + 1} pessoa -------------')
    nome = str(input(f'Informe o nome: ')).strip()
    idade = int(input(f'Informe a idade: '))
    sexo = str(input('Sexo [M] / [F] ? ')).strip()
    somaIdades += idade
    if c == 1 and sexo in 'Mm':  # preenche as variáveis na primeira rodada do for
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > idadeMaisVelho:
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        somaMulher += 1
print(f'A média das idades é {somaIdades / 4:.1f}')
print(f'O homem mais velho tem {idadeMaisVelho} anos e se chama {nomeMaisVelho}.')
print(f'Ao todo são {somaMulher} mulheres com menos de 20 anos.')
