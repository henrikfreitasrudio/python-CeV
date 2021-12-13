inverso = ''
frase = str(input('Digite uma palavra: ')).strip().upper()
palavras = frase.split()  # separa a frase em palavras numa "lista"
junto = ''.join(palavras)  # junta todas as palavras sem espaços
for letra in range(len(junto) - 1, -1, -1):  # [len(junto) - 1] para desconsiderar o zero que o FOR considera!!
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if junto == inverso:
    print('Temos um PALÍNDROMO!!')
else:
    print('A frase digitada não é um palíndromo!')
