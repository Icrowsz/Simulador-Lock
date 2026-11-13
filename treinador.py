from pessoa import Pessoa


class Treinador(Pessoa):
    def __init__(self, nome, idade, filosofia):
        super().__init__(nome, idade)
        self.filosofia = filosofia

    def apresentar(self):
        return f"[Treinador] {super().apresentar()} | Filosofia: {self.filosofia}"
