# Um dicionário é uma lista de chave e valor.

a = {1: 'Maria', 2: 'João', 3: 'Pedro'}

print(a)
print(a[1]) # Retorna o elemento da chave passado

a.popitem() # Remove o ultimo item(chave e valor) do dicionário
print(a)

a.pop(1) # Remove o item da chave passada
print(a)

a.clear()
print(a)
