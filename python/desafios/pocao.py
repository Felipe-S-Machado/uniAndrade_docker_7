class Pocao:
    """Classe genérica para poções de Cura ou Veneno."""
    def __init__(self, tipo: str, potencia: int):
        self.tipo = tipo.title()
        self.potencia = potencia


class Personagem:
    """Representa um personagem com nome, saúde e estado de vida."""
    def __init__(self, nome: str):
        self.nome = nome
        self.saude = 20
        self.vivo = True

    def usar_pocao(self, pocao: Pocao) -> None:
        # Bloqueia outras poções se estiver morto
        if not self.vivo:
            print(f"{self.nome} está morto e não pode usar poções.")
            return

        # Poção de cura
        if pocao.tipo.lower() == "cura":
            cura_possivel = min(pocao.potencia, 20 - self.saude)
            if cura_possivel <= 0:
                print(f"{self.nome} não precisa se curar. Saúde já está em {self.saude}.")
            else:
                self.saude += cura_possivel
                print(f"{self.nome} usou poção de {pocao.tipo} e recuperou {cura_possivel} de vida (saúde: {self.saude}).")

        # Poção de veneno
        elif pocao.tipo.lower() == "veneno":
            dano = 15
            if self.saude - dano <= 0:
                self.saude = 0
                self.vivo = False
                print(f"{self.nome} usou poção de {pocao.tipo} e recebeu {dano} de dano (saúde: {self.saude}).")
                print(f"{self.nome} morreu.")
                mostrar_status(self)
            else:
                self.saude -= dano
                print(f"{self.nome} usou poção de {pocao.tipo} e recebeu {dano} de dano (saúde: {self.saude}).")

# Se o personagem ainda está vivo, decremente ao usar poção veneno
# Pode usar poção veneno
# Pode usar poção saúde
# Se a saúde for <= 0
#   personagem vivo = False
#   informe que o personagem está morto e cancele a possibilidade de incrementar ou decrementar saúde


def mostrar_menu() -> None:
    """Exibe o menu principal do jogo."""
    print("""
+===========================================+
|               MENU DO JOGO                |
+===========================================+
| 1 - Usar Poção de Cura                    |
| 2 - Usar Poção de Veneno                  |
| 3 - Mostrar Status                        |
| 4 - Sair                                  |
+===========================================+
""")


def mostrar_status(personagem: Personagem) -> None:
    """Mostra o status atual do personagem."""
    estado = "vivo" if personagem.vivo else "morto"
    print(f"\n{personagem.nome} - Saúde: {personagem.saude} - Estado: {estado}\n")


def processar_escolha(
    escolha: str,
    personagem: Personagem,
    pocao_cura: Pocao,
    pocao_veneno: Pocao
) -> bool:
    """
    Processa a opção escolhida pelo player no menu.
    """
    if escolha == "1":
        personagem.usar_pocao(pocao_cura)
    elif escolha == "2":
        personagem.usar_pocao(pocao_veneno)
    elif escolha == "3":
        mostrar_status(personagem)
    elif escolha == "4":
        print("Saindo do jogo. Até mais!")
        return False
    else:
        print("Opção inválida. Tente novamente.")
    return True


if __name__ == "__main__":
    p1 = Personagem("Chaves")
    pocao_cura = Pocao("Cura", 15)
    pocao_veneno = Pocao("Veneno", 15)

    rodando = True
    while rodando:
        mostrar_menu()
        escolha = input("Escolha uma opção (1-4): ")
        rodando = processar_escolha(escolha, p1, pocao_cura, pocao_veneno)
