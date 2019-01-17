# Variável é um espaço de memória que reservamos para armazenar 
# valores temporários que estão sendo processados ou manipulados.
# String é um conjunto de caracteres.
txt = 'Strings'
print(txt)

num = float(input('Digite um número: '))
print('='*3 + ' O número digitado foi {:.1f}! '.format(num) + '='*3)
print('O dobro de {} é: {}'.format(num, (num*2)))
#print("Teste {numero}".format(numero=num))
print('{} é do tipo: {}'.format(num, type(num)))
