n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/ 2
print(f'A média entre {n1:.1f} e {n2:.1f} é {m:.1f}.')
if m >= 7:
    print('O aluno está APROVADO!!')
elif 5 <= m < 6.95:
        print('O aluno está de RECUPERAÇÃO!!')
elif m < 5:
    print('O aluno está REPROVADO!!')
