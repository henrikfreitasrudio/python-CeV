peso = float(input('Peso: (Kg) '))
alt = float(input('Altura: (m) '))
imc = peso / (alt ** 2)
print(f'O seu IMC = {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= imc <= 30:
    print('Você está com SOBREPESO!')
elif imc <= 40:
    print('Você está com OBESIDADE!')
elif imc > 40:
    print('Você está com OBESIDADE MÓRBIDA, cuidado!')
