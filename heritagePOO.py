#import classes -  ai teria que fazer classes.Aluno, classes.medtodo()
from classes import * # asterisco importa tudo

def main():
    a1= Aluno("pedro", 19, "informatica", "T01")
    a1.aniversario()
    a1.fazer_matricula()
    a1.estudar()
    print(a1)

if __name__=="__main__":
    main()