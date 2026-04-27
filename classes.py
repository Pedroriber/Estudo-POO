from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.idade=idade
        self.nome= nome

    def aniversario(self):
        self.idade+=1

    @abstractmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso=curso
        self.turma=turma
    def __str__(self):
        return f"Aluno: {self.nome}, idade: {self.idade}, Curso: {self.curso}"
    def fazer_matricula(self):
        print( f"{self.nome} fez matricula")

    def estudar(self):
        print(f"{self.nome} estuda na turma {self.turma}")
    
class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade= especialidade
        self.nivel=nivel
    
    def dar_aula(self):
        return f"{self.nome} deu aula"
    
    def estudar(self):
        pass

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo= cargo
        self.setor=setor

    def bater_ponto(self):
        return f"{self.nome} bateu ponto"
    
    def estudar(self):
        pass