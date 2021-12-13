cont = pessoas_maior = masc = mulher_menor = 0
while True:
    print('-' * 25)
    print(f'Cadastro da {cont + 1}ª pessoa:')
    print('-' * 25)
    idade = int(input(f'Informe a idade: '))
    cont += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        pessoas_maior += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        mulher_menor += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Ao todo, {pessoas_maior} pessoas tem mais de 18 anos.')
print(f'Foram cadastrados {masc} homens.')
print(f'{mulher_menor} mulheres com menos de 20 anos.')
print('Fim!!')
