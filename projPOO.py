class Gafanhoto:
    def __init__(self):
        self.nome=""
        self.idade=0

    def aniversario(self):
        self.idade= self.idade+1    

    def mensagem (self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade"
obj= Gafanhoto()
obj.nome="Pedro"
obj.idade=19
obj.aniversario()

obj2= Gafanhoto()
obj2.nome="Laura"
obj2.idade=54
obj2.aniversario()
print(obj.mensagem())
print(obj2.mensagem())

