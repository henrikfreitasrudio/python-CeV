peso_maior = 0
peso_menor = 0
for c in range(0, 5):
    peso = float(input(f'Informe o peso da {c + 1}ª pessoa: '))
    if c == 0:  # primeira rodada
        peso_menor = peso
        peso_maior = peso
    else:  # demais rodadas do laço
        if peso > peso_maior:  # maior peso
            peso_maior = peso
        if peso < peso_menor:  # menor peso
            peso_menor = peso
print(f'O maior peso lido foi {peso_maior:.1f}kg.')
print(f'E o menor foi {peso_menor:.1f}kg.')
