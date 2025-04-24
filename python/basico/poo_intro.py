class Player:
    host = "localhost:8080" #global
    #inicializador do objeto
    #passando valores posicionais
    def __init__(self, nome, arma):
        self.__nome = nome #autoriza modificação/objeto
        self.__arma = arma

    #getter e setter (fake)
    #getter = metodo que intercepta a visualização
    def get_nome(self):
        print(f"Nome: {self.__nome}")

    # def set_nome(it, nome):
    #      it.nome = nome

    def set_nome(self, arma):# metodo convencional e mais utilizado pela comunidade
          self.arma = arma

    def get_arma(self):
        print(f"Nome: {self.__arma}")

    # def set_nome(it, nome):
    #      it.nome = nome
    def set_arma(self, arma):# metodo convencional e mais utilizado pela comunidade
          self.arma = arma

# personagem1 = Player ("torfin", "adagas")
# personagem2 = Player ("rimuro", "espada")

# print(personagem1.nome, "\n", personagem2.nome)

aquiles: Player = Player ('Aquiles', 'espada')

kratos: Player = Player ('Kratos', 'Knifa')
# print(kratos.nome, kratos.arma)
# print(Player.arma)
# print(Player.host)
# print(aquiles.host)
# print("Aquiles:"+aquiles.host)
print(kratos.set_nome("Vivaldi"))
print(kratos.get_nome())
