class Gafanhoto:
    '''
Pedro
    '''

    def __init__(self, nome="vazio", idade=0):
        self.nome= nome
        self.idade=idade 

    def aniversario(self):
        self.idade= self.idade+1    

    #def mensagem (self):
    #    return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade"
    
    def __str__(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade"
obj= Gafanhoto("Pedro", 19)
obj.aniversario()

obj2= Gafanhoto("Laura", 54)
obj2.aniversario()
#print(obj.mensagem())
print(obj)

print(obj2)

obl3= Gafanhoto()
print(obl3)

print(obj.__doc__)
print(obj.__dict__)
print(obj.__getstate__())
print(obj.__class__)


