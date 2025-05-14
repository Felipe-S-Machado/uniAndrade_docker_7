class Personagem:
        def __init__(self, nome):
            self.nome = nome
            self.saude = 5
            self.vivo = True
            
        def usar_pocao(self, pocao):
            
            if (pocao.tipo == "Cura"):
                if (self.saude + pocao.potencia > 100):
                    print("Nao precisar beber, saude vai ficar maior que 100")
                else: 
                    self.saude += pocao.potencia
                    print(f"Personagem{self.nome} usou poção {pocao.tipo}")
                    print(f"Curou {pocao.potencia} de saude {self.saude}")
            else:
                if (self.saude - pocao.potencia <= 0):
                    print("Voce morreu")
                    return
                else: 
                    self.saude -= pocao.potencia
                    print(f"Personagem{self.nome} usou poção {pocao.tipo}")
                    print(f"Dano {pocao.potencia} saude {self.saude}")
            
            
class PocaoVerde:
        def __init__(self, tipo, potencia):
            self.tipo = tipo
            self.potencia = potencia

class PocaoRoxa:
        def __init__(self, tipo, potencia):
            self.tipo = tipo
            self.potencia = potencia
    
# instanciar Jogador
p1 = Personagem("Chaves")
pocao1 = PocaoVerde("Cura", 15)
pocao2 = PocaoRoxa("Veneno", 20)

p1.usar_pocao(pocao1)
p1.usar_pocao(pocao2)


# Se o persagem ainda está vivo, decremente ao usar poção veneno
    # Pode usar poção veneno
    # Pode usar poção saude
# Se a saúde for <= 0 
    # personagem vivo=False)
    # informe personagem está morto, foi de "arrasta"
    # cancele a possibilidade de incrementar ou decrementar saúde