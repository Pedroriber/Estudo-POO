""" class Pessoa:
    def __init__(self, idade):
        self.idade = idade

p = Pessoa(18)
p.idade = -5  # 😬 valor inválido """

""" class Pessoa:
    def __init__(self, idade):
        self._idade = idade  # "_" indica uso interno

    def set_idade(self, idade):
        if idade >= 0:
            self._idade = idade

    def get_idade(self):
        return self._idade """

class Pessoa:
    def __init__(self, idade):
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = valor

p = Pessoa(18)
p.idade = -5
print(p.__dict__)