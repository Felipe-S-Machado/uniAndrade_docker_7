class PersonagemGame:
    def __init__(self, nome, classe, defesa, vida):
        self.nome = nome
        self.classe = classe
        self.defesa = defesa
        self.vida = vida
        self.inventario = {}

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Classe: {self.classe}, Defesa: {self.defesa}, Vida: {self.vida}")

    def adicionar_item(self, item, quantidade=1):
        if item in self.inventario:
            self.inventario[item] += quantidade  
        else:
            self.inventario[item] = quantidade

    def exibir_inventario(self):
        if self.inventario:
            print(f"Inventário de {self.nome}:")
            for item, quantidade in self.inventario.items():
                print(f" - {quantidade}x {item}")
        else:
            print(f"O inventário de {self.nome} está vazio.")

personagem1 = PersonagemGame("Lancelot", "Espadachim", 18, 80)
personagem2 = PersonagemGame("Tristan", "Guerreiro", 16, 65)

personagem1.adicionar_item("Armadura de placas", 1)
personagem1.adicionar_item("Espada Longa", 1)

personagem2.adicionar_item("Arco Longo", 1)
personagem2.adicionar_item("Aljava", 1)
personagem2.adicionar_item("Flecha", 50)


personagem1.exibir_dados()
personagem1.exibir_inventario()
print("\n")
personagem2.exibir_dados()
personagem2.exibir_inventario()
