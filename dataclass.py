from dataclasses import dataclass


@dataclass
class Pessoa():
    nome: str 
    idade: int 

    def aniversario(self):
        self.idade+=1

    def estudar(self):
        pass

@dataclass
class Aluno(Pessoa):
    curso: str
    turma: str
    def __str__(self):
        return f"Aluno: {self.nome}, idade: {self.idade}, Curso: {self.curso}"
    def fazer_matricula(self):
        print( f"{self.nome} fez matricula")

    def estudar(self):
        print(f"{self.nome} estuda na turma {self.turma}")

@dataclass 
class Professor(Pessoa):
  
    especialidade: str
    nivel: str
    
    def dar_aula(self):
        return f"{self.nome} deu aula"
    
    def estudar(self):
        pass

@dataclass
class Funcionario(Pessoa):
    cargo: str
    setor: str

    def bater_ponto(self):
        return f"{self.nome} bateu ponto"
    
    def estudar(self):
        pass

def main():
    a1= Aluno("pedro", 19, "informatica", "T01")
    a1.aniversario()
    a1.fazer_matricula()
    a1.estudar()
    print(a1)

if __name__=="__main__":
    main()