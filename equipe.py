class Equipe:
    TAMANHO = 6

    def __init__(self, nome, treinador):
        self.nome = nome
        self.treinador = treinador      # associação
        self._jogadores = []            # agregação

    @property
    def jogadores(self):
        return list(self._jogadores)

    @property
    def goleiro(self):
        return next((j for j in self._jogadores if j.posicao == "Goleiro"), None)

    def adicionar_jogador(self, jogador):
        if jogador in self._jogadores:
            raise ValueError(f"{jogador.nome} já está na equipe.")
        if len(self._jogadores) >= self.TAMANHO:
            raise ValueError(f"A equipe já tem {self.TAMANHO} jogadores.")
        if jogador.posicao == "Goleiro" and self.goleiro:
            raise ValueError("A equipe já tem um goleiro.")
        self._jogadores.append(jogador)

    def validar(self):
        if len(self._jogadores) != self.TAMANHO:
            raise ValueError(f"{self.nome} precisa de {self.TAMANHO} jogadores (tem {len(self._jogadores)}).")
        if not self.goleiro:
            raise ValueError(f"{self.nome} precisa de um goleiro.")

    def por_posicao(self, *posicoes):
        return [j for j in self._jogadores if j.posicao in posicoes]

    def __str__(self):
        return f"{self.nome} (técnico: {self.treinador.nome}, {len(self._jogadores)}/{self.TAMANHO} jogadores)"
