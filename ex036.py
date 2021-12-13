valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
ano = int(input('Financiamento em quantos anos? '))
prest_mensal = (valor / (ano*12))
min = sal * 0.30
print(f'Para pagar uma casa de R${valor:.2f} em {ano} anos, a prestação será de R${prest_mensal:.2f}')
if prest_mensal <= min:
    print('Financiamento pode ser APROVADO!')
else:
    print('Financiamento não pode ser APROVADO!')
