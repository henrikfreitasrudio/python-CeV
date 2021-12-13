tabela = ('Internacional', 'São Paulo',	'Flamengo',	'Atlético-MG', 'Palmeiras',	'Grêmio',
          'Fluminense',	'Ceará', 'Corinthians',	'Santos', 'Bragantino',	'Athético-PR',
          'Atlético-GO', 'Sport', 'Vasco', 'Fortaleza', 'Bahia', 'Goiás', 'Coritiba',
          'Botafogo')
print(f'A lista da tabela é: {tabela}')
print('+=' * 100)
print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print('+=' * 100)
print(f'Os 4 ultimos colocados são: {tabela[-4:]}')
print('+=' * 100)
print(f'Os times em ordem alfabética são: {sorted(tabela)}')
print('+=' * 100)
pos_f = tabela.index('Flamengo')
print(f'O flamengo está na posição {pos_f + 1}!')
