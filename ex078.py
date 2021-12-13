cont = 0
nomes = ('Henrik', 'Leticia', 'Caik', 'Felipe', 'Antonio', 'Luzia')
for palavra in nomes:
    print(f'\nO nome {palavra.upper()} possui as vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end='')
