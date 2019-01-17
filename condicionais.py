a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))

if a > b:
    print('{} é maior que {}'.format(a,b))
elif b > a:
    print('{} é maior que {}'.format(b,a))
else:
    print('Não encontrado')
