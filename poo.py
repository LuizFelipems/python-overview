class Dog(object):
    # name = 'rex' # Define um atributo a classe
    def __init__(self, name='Toto'): # Define um construtor da classe
        self.name = name # Define um atributo a instância da classe
    
    def latir(self, vezes=2):
        print('Au!' * vezes)
    

# obj = Dog() # Instânciou um objeto da classe
# obj.name = 'Toto' # Atribuiu um nome a parâmetro á instância da classe
# print(obj.name) # Acessa o atributo da instância    
# obj.latir() # Chama a função da instância do objeto

class SaoBernardo(Dog): # Herdando da classe Dog
    def __init__(self, idade=1):
        super().__init__()
        self.idade = idade

    def latir(self, vezes=1):
        print('Au!' * vezes)
c = SaoBernardo(2)
c.latir(10)
print(c.name)
print(c.idade)
