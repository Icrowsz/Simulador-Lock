from pessoa import Pessoa

POSICOES = ["Atacante", "Meio-campista", "Ala", "Zagueiro", "Goleiro"]


class Jogador(Pessoa):
    def __init__(self, nome, idade, posicao, chute, passe, velocidade, defesa):
        super().__init__(nome, idade)
        if posicao not in POSICOES:
            raise ValueError(f"Posição inválida: {posicao}")
        for atributo in (chute, passe, velocidade, defesa):
            if not 0 <= atributo <= 100:
                raise ValueError("Os atributos precisam estar entre 0 e 100.")
        self.posicao = posicao
        self.chute = chute
        self.passe = passe
        self.velocidade = velocidade
        self.defesa = defesa

    def apresentar(self):
        return (f"[Jogador] {super().apresentar()} | {self.posicao} | "
                f"CHU {self.chute} PAS {self.passe} VEL {self.velocidade} DEF {self.defesa}")
