import random
from duelo import vence, chance_ataque
from estatistica import Estatistica
import frases
import papeis


class Partida:
    LANCES = 30
    DETALHADO = False  # True mostra todos os lances (desarmes, bloqueios...)

    def __init__(self, casa, visitante):
        casa.validar()
        visitante.validar()
        nomes_casa = {j.nome for j in casa.jogadores}
        repetidos = nomes_casa & {j.nome for j in visitante.jogadores}
        if repetidos:
            raise ValueError("Jogador(es) nas duas equipes: " + ", ".join(sorted(repetidos)))
        self.casa = casa
        self.visitante = visitante
        self.eventos = []
        self._gols = {casa: 0, visitante: 0}
        # COMPOSIÇÃO: as Estatisticas nascem e morrem com a partida
        self._estatisticas = {j: Estatistica() for j in casa.jogadores + visitante.jogadores}

    # ---------- consultas ----------
    def placar(self):
        return self._gols[self.casa], self._gols[self.visitante]

    def estatisticas(self):
        """Lista de (equipe, jogador, Estatistica)."""
        return [(eq, j, self._estatisticas[j])
                for eq in (self.casa, self.visitante) for j in eq.jogadores]

    # ---------- simulação ----------
    def simular(self):
        for lance in range(1, self.LANCES + 1):
            minuto = lance * 3
            ataque, defesa = random.choice([(self.casa, self.visitante), (self.visitante, self.casa)])
            self._jogar_lance(minuto, ataque, defesa)

    def _narrar(self, minuto, texto, importante=False):
        """Só gols e defesas importantes aparecem, a menos que DETALHADO seja True.
        Cada evento é (texto, destaque); destaque=True é usado para pintar de verde."""
        if importante or self.DETALHADO:
            self.eventos.append((f"{minuto:02d}' {texto}", importante))

    def _jogar_lance(self, minuto, ataque, defesa):
        finalizador = papeis.escolher(ataque.jogadores, "finalizar")
        assistente = None
        lance_assistencia = None
        if random.random() < 0.25:
            self._narrar(minuto, f"{finalizador.nome} ({ataque.nome}) parte sozinho para a finalização!")
        else:
            construtor = papeis.escolher(ataque.jogadores, "construir", excluir=finalizador)
            lance_assistencia = self._construir(minuto, construtor, ataque, defesa)
            if lance_assistencia is None:
                return
            assistente = construtor
        self._finalizar(minuto, finalizador, assistente, lance_assistencia, ataque, defesa)

    def _construir(self, minuto, construtor, ataque, defesa):
        if construtor.posicao == "Ala":
            lance = random.choice(["drible", "cruzamento"])
        elif construtor.posicao == "Meio-campista":
            lance = random.choice(["troca de passe", "cruzamento longo"])
        else:  # atacante ou zagueiro fazendo um passe
            lance = "passe"
        # drible usa Velocidade; os outros lances usam Passe
        base = construtor.velocidade if lance == "drible" else construtor.passe
        forca = base * papeis.fator(construtor, "construir")
        marcador = papeis.escolher(defesa.jogadores, "defender")
        forca_marcador = marcador.defesa * papeis.fator(marcador, "defender")
        if vence(forca, forca_marcador):
            self._narrar(minuto, f"{construtor.nome} ({ataque.nome}) passa por {marcador.nome} com {lance}!")
            return lance
        self._narrar(minuto, f"{marcador.nome} ({defesa.nome}) corta o {lance} de {construtor.nome}.")
        return None

    def _finalizar(self, minuto, finalizador, assistente, lance_assistencia, ataque, defesa):
        # Só descrição: a mecânica é a mesma para os dois tipos
        tipo = random.choice(["chuta direto", "finaliza de voleio"])
        forca_chute = finalizador.chute * papeis.fator(finalizador, "finalizar")
        bloqueador = papeis.escolher(defesa.jogadores, "defender")
        if not vence(forca_chute, bloqueador.defesa * papeis.fator(bloqueador, "defender")):
            self._estatisticas[bloqueador].defesas += 1
            self._narrar(minuto, f"{finalizador.nome} {tipo}... mas {bloqueador.nome} bloqueia!")
            return
        goleiro = defesa.goleiro
        dados = {"f": finalizador.nome, "g": goleiro.nome, "t": ataque.nome}
        if vence(forca_chute, goleiro.defesa):
            self._gols[ataque] += 1
            self._estatisticas[finalizador].gols += 1
            if assistente:
                self._estatisticas[assistente].assistencias += 1
                dados["a"] = assistente.nome
                contexto = random.choice(frases.ASSISTENCIA[lance_assistencia])
            else:
                contexto = random.choice(frases.INDIVIDUAL)
            self._narrar(minuto, contexto.format(**dados), importante=True)
            self._narrar(minuto, f"GOL do {ataque.nome}! " + random.choice(frases.GOL[tipo]).format(**dados),
                         importante=True)
        else:
            self._estatisticas[goleiro].defesas += 1
            self._narrar(minuto, "DEFESA! " + random.choice(frases.DEFESA_GOLEIRO[tipo]).format(**dados),
                         importante=True)
