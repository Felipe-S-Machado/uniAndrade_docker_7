# from itens import arma, armadura, pocao
# print(arma.Arma("espada").usar())
# from itens import *
from itens import Arma, Armadura, Pocao

def main():
    faca = Arma("Tramontina")
    faca.usar()

    couro = Armadura("Couro")
    couro.usar()

    cura = Pocao("Cura")
    cura.usar()

if __name__ =="__main__":
    main()
