print('-=' * 20)
print(f'{"LOJAS FREITAS":*^40}')
print('-=' * 20)
valor = float(input('Qual o valor do produto? R$'))
cond = int(input('''Condição de pagamento:
[ 1 ] À vista, dinheiro / cheque
[ 2 ] À vista no cartão 
[ 3 ] Em até 2x no cartão 
[ 4 ] 3X ou mais no cartão
Qual sua opção? '''))
if cond == 1: # 10% de desconto
    ad = valor - (valor * 0.10)
elif cond == 2: # 5% de desconto
    ad = valor - (valor * 0.05)
elif cond == 3: # valor real em 2X
    ad = valor
    parc = valor / 2
    print(f'Sua compra será parcelada em R${parc:.2f}, SEM JUROS.')
elif cond == 4: # 20% de juros
    ad = valor + (valor * 0.20)
    totparcelas = int(input('Quantas parcelas? '))
    parcela = ad / totparcelas
    print(f'Sua compra será parcelada em {totparcelas}X de R${parcela:.2f}, COM JUROS.')
else:
    ad = valor
    print('Opção inválida de pagamento. Tente novamente')
print(f'Sua compra de R${valor:.2f} vai custar R${ad:.2f} no final.')
