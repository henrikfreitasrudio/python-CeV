frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra) # Junta as palavra sem espaços
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}.')
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
