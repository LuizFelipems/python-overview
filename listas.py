# Uma Lista é uma estrutura que pode conter itens.

a = [1,2,2,2,4]
print(a)
a[4] = 5 # Adiciona um item no index passado
# a.append(('texto', 4, 4)) # Adiciona um item no final da lista
a.append(4) 

print(a.count(2)) # Quantas vezes o elemento aparece
print(a.index(2)) # Retorna o primeiro index do elemento passado

a.insert(0,5) # Adiciona um objeto no index passado
print(a)

a.reverse() # Ordena o reverso
print(a)

a.sort() # Ordena crescente, com objetos só do mesmo tipo
print(a)
