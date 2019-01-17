lista = ['Grêmio', 'Vasco', 'Palmeiras']

i = 0
while i < len(lista):
    print(lista[i])
    i+=1
else: # Será executado caso não encontre o break, ou a condição seja falsa
    print(lista)

conta = 0
while(conta <= 10):
    conta += 1
    print(conta)
else: # Será executado caso não encontre o break, ou a condição seja falsa
    print("Valor da variável conta é: ", conta)