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

print(obj.mensagem())
