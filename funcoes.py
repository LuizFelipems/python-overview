def somar(total, num=2): # num é um parâmetro opicional
    return total + num

print(somar(5)) # chamando função e passando argumentos

print(somar(total=10))

d = {'total': 1, 'num': 4}
print(somar(**d)) # ** Avisa ao python para fazer a interação do dicionário

# Funções que aceitem outras funções como argumentos são chamadas 
# high-order functions.

def calculo(val1, val2, func):
    return func(val1, val2)

def soma(a, b):
    return a + b

def multiplica(a, b):
    return a * b

opcao = 'multiplica'
if opcao == 'soma':
    print(calculo(10,7,soma))
elif opcao == 'multiplica':
    print(calculo(10,2,multiplica))

