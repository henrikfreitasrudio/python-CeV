from datetime import date
ano_nasc = int(input('Informe o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'Você tem {idade} anos.')
if idade <= 9:
    clas = 'mirim'
elif idade <= 14:
    clas = 'infantil'
elif idade <= 19:
    clas = 'junior'
elif idade <= 25:
    clas = 'sênior'
else:
    clas = 'master'
print(f'Sua classificação é {clas.upper()}.')
