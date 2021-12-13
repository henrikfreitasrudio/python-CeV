from random import randint
from time import sleep
print('-=' * 12)
print(f'{"SEJA BEM-VINDO AO JOKENPÔ"}')
print('-=' * 12)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 15)
print(f'O computador jogou {itens[computador]}.')
print(f'O jogador jogou {itens[jogador]}')
print('-=' * 15)
if computador == 0: # computador joga PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCE!')
    elif jogador == 2:
        print('Computador VENCE!')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 1: # computador joga PAPEL
    if jogador == 0:
        print('Computador VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador VENCE!')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 2: # computador joga TESOURA
    if jogador == 0:
        print('Jogador VENCE!')
    elif jogador == 1:
        print('Computador VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada INVÁLIDA!')
