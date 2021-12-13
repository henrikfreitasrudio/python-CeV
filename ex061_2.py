# Gerador de PA usando for novamente
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
fim = primeiro + (10 * razao)
for c in range(primeiro, fim, razao):
    print(c, end=' -> ')
print('FIM.')
