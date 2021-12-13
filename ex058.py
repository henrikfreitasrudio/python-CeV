from random import randint
cont = 0
computador = randint(0, 10)
print('Olá, eu sou o seu computador... Pensei em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
resultado = False  # o resultado inicia como falso
while not resultado:  # enquanto o resultado for "não falso", ou seja, verdadeiro...
    jogador = int(input('Seu palpite: '))
    cont += 1
    if computador == jogador:
        resultado = True
    else:
        if jogador > computador:
            print('MENOS...')
        elif jogador < computador:
            print('MAIS...')
print(f'Você acertou com {cont} palpites. Parabéns!!')
