from datetime import date
sex = str(input('Informe o sexo: [M] ou [F]: '))
if sex.upper() in 'M':
    ano_nasc = int(input('Informe o ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    print(f'Quem nasceu em {ano_nasc} terá {idade} anos em {ano_atual}.')
    if idade == 18:
        print('Você deve se alistar imediatamente!!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} anos.')
        print(f'Seu alistamento será em {ano_atual + saldo}.')
    elif idade > 18:
        saldo = idade - 18
        print(f'Você deveria ter se alistado há {saldo} anos.')
        print(f'Seu alistamento foi em {ano_atual - saldo}')
else:
    print('Mulher não precisa se alistar!!!')
