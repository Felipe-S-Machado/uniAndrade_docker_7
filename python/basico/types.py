# print(type("na"))
# print(type(1))
# print(type(0.5))
# print(type(True))

class A:
    ... #elipeses

class B:
    pass #elipeses

class C(A, B):
    ... #elipeses

#Type anotations

idade: int = 32
salario: float = 35000.50
nome: str = "Julios"
casado: bool = True
dados: dict = {"nome": nome, "salario": salario, "idade": idade}
array: list = [2,5,"ju",25,25,25]
tupla: tuple = (2,5,25,25)
unico: set = {2,5,"ju",25,25,25}

#print (unico)
#print(nome.upper()) #metodo builtin
#print(vars(C))      #imprime class com dict
#help(C)             #ajuda a ver internamente

nome: str = 'Ana paula'
eh_casado: bool = True

pessoa: A = A()     #tipo personalizado
A.nome = "maria"    #atribuição direto na classe
A.cargo = "diretor" 

print(A.__dict__)   #armazena valores da class
