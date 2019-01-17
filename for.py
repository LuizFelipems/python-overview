lista = ['Grêmio', 'Vasco', 'Palmeiras']

for time in lista:
    print(time)
    if time == 'São Paulo':
        break
else: # Será executado caso não encontre o break
    print(lista)
