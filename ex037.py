n = int(input('Informe um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Escolha sua opção: '))
if opcao == 1:
    print(f'{n} convertido para BINÁRIO é {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} convertido para OCTAL é {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} convertido para HEXADECIMAL é {hex(n)[2:]}')
else:
    print('Opção inválida!!')
