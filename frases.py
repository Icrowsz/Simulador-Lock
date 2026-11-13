"""Frases pré-definidas da narração.
Marcadores: {f} finalizador, {a} assistente, {g} goleiro, {t} time que ataca."""

# Linha que antecede o gol, conforme o lance que originou a assistência
ASSISTENCIA = {
    "troca de passe": [
        "{a} troca passes rápidos e deixa {f} em ótima posição.",
        "{a} toca de primeira e coloca {f} cara a cara com o gol.",
        "{a} enfia uma bola açucarada para {f}.",
        "Jogada trabalhada! {a} acha {f} livre na entrada da área.",
    ],
    "cruzamento longo": [
        "{a} lança uma bola longa e precisa na direção de {f}.",
        "{a} cruza em curva, de longe, para {f}.",
        "Bola alta na área! {a} serve {f} no ponto certo.",
        "{a} acha um passe de 40 metros para {f}.",
    ],
    "cruzamento": [
        "{a} vai à linha de fundo e cruza rasteiro para {f}.",
        "{a} levanta a bola na área e {f} aparece livre.",
        "Cruzamento venenoso de {a} para {f}!",
        "{a} cruza com categoria na cabeça de {f}.",
    ],
    "drible": [
        "{a} deixa o marcador sentado e serve {f}.",
        "{a} arranca num drible desconcertante e rola para {f}.",
        "{a} passa por dois e deixa {f} sozinho.",
        "Velocidade pura! {a} se livra da marcação e acha {f}.",
    ],
    "passe": [
        "{a} sai jogando e encontra {f} em boa posição.",
        "{a} toca para {f}, que fica de frente para o gol.",
    ],
}

# Linha que antecede o gol quando não houve assistência
INDIVIDUAL = [
    "{f} recebe a bola e parte sozinho em direção ao gol!",
    "{f} ganha na corrida e fica de frente para o goleiro!",
    "{f} resolve por conta própria e invade a área!",
    "{f} domina, vira o corpo e finaliza sem pensar duas vezes!",
]

GOL = {
    "chuta direto": [
        "{f} bate firme no canto e a rede balança!",
        "{f} chuta forte, sem chance para {g}!",
        "{f} finaliza colocado e {g} só vê a bola entrar!",
        "{f} dispara um petardo no ângulo!",
        "{f} bate cruzado e estufa a rede!",
    ],
    "finaliza de voleio": [
        "{f} acerta um voleio perfeito, {g} não alcança!",
        "{f} emenda de voleio e faz um golaço!",
        "{f} bate de voleio, a bola explode no fundo da rede!",
        "{f} sobe e finaliza de voleio, que pintura!",
        "{f} acerta um voleio colocado no canto de {g}!",
    ],
}

DEFESA_GOLEIRO = {
    "chuta direto": [
        "{g} se estica todo e espalma o chute de {f}!",
        "{g} voa no canto e evita o gol de {f}!",
        "{f} bate forte, mas {g} segura firme!",
        "{g} faz uma defesa difícil e salva o time!",
        "{g} fecha o ângulo e pega o chute de {f}!",
    ],
    "finaliza de voleio": [
        "{f} tenta um voleio, mas {g} defende com a ponta dos dedos!",
        "{g} espalma o voleio de {f} para escanteio!",
        "{g} faz um milagre no voleio de {f}!",
        "{f} acerta o voleio, mas {g} estava no lugar certo!",
        "{g} salta e desvia o voleio de {f}!",
    ],
}
