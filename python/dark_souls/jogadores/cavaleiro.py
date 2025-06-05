from jogadores.jogador import Jogador

class Cavaleiro(Jogador): #herança
    def __init__(self, nome:str, dano:int, resistencia = 85, armadura="Diamante"):
        #Jogador.__init__(nome, dano)
        self.resistencia = resistencia # atributo extra
        self.armadura = armadura # atributo extra
        super().__init__(nome, dano)
       # self.__saude = 100 # encapsulamento

    @property # decorador retorna apenas como propriedade
    def saude(self):
        return self.__saude
    
    @saude.setter # decorador retorna apenas como propriedade
    def saude(self, valor):
        self.saude += max(0, valor)
        
    def atacar(self):
        print("atacar polimorfico")
        print(f"{self.nome} atacou!")

    def defender(self):
        print("defender polimorfico")
        print(f"{self.nome} defendeu!")

if __name__ == '__main__':
    cavaleiro = Cavaleiro("Rei Arthur", 80)
    cavaleiro.atacar()