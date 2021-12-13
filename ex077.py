# Verificar a quantidade de vogais em cada palavra da tupla.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for c in p:
        if c in 'aeiou':
            print(c, end='')
