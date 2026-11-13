import banco
from jogador import Jogador, POSICOES
from treinador import Treinador
from equipe import Equipe
from partida import Partida
import visual

jogadores = []
treinadores = []
equipes = []


def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
        except ValueError:
            pass
        print(f"Digite um número de {minimo} a {maximo}.")


def escolher(lista, titulo, rotulo=lambda x: x.nome):
    if not lista:
        print(f"Nenhum item em '{titulo}'. Cadastre antes.")
        return None
    for i, item in enumerate(lista, 1):
        print(f"  {i}. {rotulo(item)}")
    return lista[ler_inteiro(f"Escolha ({titulo}): ", 1, len(lista)) - 1]


def carregar_exemplo():
    # Times do Blue Lock (Neo Egoist League / Clubes)
    bastard = [
        Jogador("Yoichi Isagi", 17, "Atacante", 90, 80, 75, 55),
        Jogador("Michael Kaiser", 19, "Atacante", 95, 75, 80, 55),
        Jogador("Alexis Ness", 17, "Meio-campista", 70, 90, 80, 55),
        Jogador("Hiori Yo", 18, "Meio-campista", 80, 90, 75, 60),
        Jogador("Jingo Raichi", 18, "Zagueiro", 70, 65, 70, 80),
        Jogador("Gin Gagamaru", 18, "Goleiro", 30, 50, 50, 95)
    ]
    
    ubers = [
        Jogador("Shoei Barou", 18, "Atacante", 95, 50, 80, 50),
        Jogador("Shuto Sendo", 18, "Atacante", 80, 75, 70, 55),
        Jogador("Niko Ikki", 16, "Meio-campista", 65, 85, 75, 80),
        Jogador("Don Lorenzo", 19, "Zagueiro", 65, 75, 85, 90),
        Jogador("Oliver Aiku", 19, "Zagueiro", 75, 65, 65, 90),
        Jogador("Gen Fukaku", 19, "Goleiro", 30, 45, 50, 85)
    ]

    pxg = [
        Jogador("Rin Itoshi", 17, "Atacante", 94, 82, 85, 60),
        Jogador("Shidou Ryusei", 18, "Atacante", 96, 60, 82, 50),
        Jogador("Charles Chevalier", 17, "Meio-campista", 75, 95, 80, 55),
        Jogador("Zantetsu Zantetsu", 18, "Ala", 78, 65, 96, 50),
        Jogador("Karasu Tabito", 18, "Zagueiro", 72, 88, 76, 80),
        Jogador("Renoir", 19, "Goleiro", 30, 45, 50, 88)
    ]

    manshine = [
        Jogador("Seishiro Nagi", 18, "Atacante", 93, 85, 75, 50),
        Jogador("Agi", 20, "Meio-campista", 82, 85, 80, 75),
        Jogador("Reo Mikage", 18, "Meio-campista", 80, 90, 82, 75),
        Jogador("Hyoma Chigiri", 18, "Ala", 86, 70, 98, 55),
        Jogador("Kazuma Nio", 18, "Zagueiro", 65, 60, 68, 85),
        Jogador("Rook", 19, "Goleiro", 30, 40, 50, 86)
    ]

    barcha = [
        Jogador("Meguru Bachira", 18, "Atacante", 88, 88, 90, 50),
        Jogador("Otoya Eita", 18, "Ala", 84, 75, 92, 55),
        Jogador("Bunny Iglesias", 18, "Atacante", 85, 75, 82, 50),
        Jogador("Ignacio Lara", 18, "Meio-campista", 78, 91, 75, 60),
        Jogador("Miroku Darai", 18, "Zagueiro", 68, 70, 72, 82),
        Jogador("Moro", 19, "Goleiro", 30, 42, 48, 85)
    ]

    # Treinadores
    noa = Treinador("Noa", 32, "Quero encontrar um rival digno")
    snuffy = Treinador("Snuffy", 37, "Futebol é um trabalho em empresa, não um esporte")
    loki = Treinador("Julian Loki", 17, "A velocidade é a chave para a evolução absoluta do futebol")
    prince = Treinador("Chris Prince", 28, "O físico perfeito cria o futebol perfeito")
    lavinho = Treinador("Lavinho", 26, "O futebol é uma arte livre e caótica baseada na imaginação")

    # Equipes
    time_bastard = Equipe("Bastard", noa)
    time_ubers = Equipe("Ubers", snuffy)
    time_pxg = Equipe("PXG", loki)
    time_manshine = Equipe("Manshine", prince)
    time_barcha = Equipe("Barcha", lavinho)

    listas_jogadores = [bastard, ubers, pxg, manshine, barcha]
    time_equipes = [time_bastard, time_ubers, time_pxg, time_manshine, time_barcha]
    lista_treinadores = [noa, snuffy, loki, prince, lavinho]

    for eq, lista in zip(time_equipes, listas_jogadores):
        for j in lista:
            eq.adicionar_jogador(j)

    all_jogadores = [j for sub in listas_jogadores for j in sub]
    jogadores.extend(all_jogadores)
    treinadores.extend(lista_treinadores)
    equipes.extend(time_equipes)
    print("Dados de exemplo carregados!")

def cadastrar_jogador():
    nome = input("Nome: ")
    idade = ler_inteiro("Idade: ", 10, 60)
    print("Posição:")
    posicao = escolher(POSICOES, "posição", rotulo=lambda p: p)
    chute = ler_inteiro("Chute (0-100): ", 0, 100)
    passe = ler_inteiro("Passe (0-100): ", 0, 100)
    velocidade = ler_inteiro("Velocidade (0-100): ", 0, 100)
    defesa = ler_inteiro("Defesa (0-100): ", 0, 100)
    jogadores.append(Jogador(nome, idade, posicao, chute, passe, velocidade, defesa))
    print("Jogador cadastrado.")


def cadastrar_treinador():
    treinadores.append(Treinador(input("Nome: "), ler_inteiro("Idade: ", 18, 90), input("Filosofia: ")))
    print("Treinador cadastrado.")


def criar_equipe():
    treinador = escolher(treinadores, "treinador")
    if treinador:
        equipes.append(Equipe(input("Nome da equipe: "), treinador))
        print("Equipe criada.")


def adicionar_jogador_equipe():
    equipe = escolher(equipes, "equipe")
    jogador = escolher(jogadores, "jogador", rotulo=lambda j: f"{j.nome} ({j.posicao})") if equipe else None
    if equipe and jogador:
        try:
            equipe.adicionar_jogador(jogador)
            print(f"{jogador.nome} entrou no {equipe.nome}.")
        except ValueError as erro:
            print(erro)


def _linha_jogador(j):
    return [j.nome, j.posicao, j.chute, j.passe, j.velocidade, j.defesa]


CABECALHO_JOGADOR = ["Jogador", "Posição", "Chute", "Passe", "Veloc.", "Defesa"]


def listar_equipes():
    if not equipes and not jogadores:
        print("Nada cadastrado ainda.")
        return
    for equipe in equipes:
        print(f"\n{visual.amarelo(equipe.nome)}  |  Técnico: {equipe.treinador.nome}"
              f"  |  {len(equipe.jogadores)}/{equipe.TAMANHO} jogadores")
        print(f"Filosofia: {equipe.treinador.filosofia}")
        visual.tabela([_linha_jogador(j) for j in equipe.jogadores], CABECALHO_JOGADOR)
    jogadores_livres = [j for j in jogadores if not any(j in e.jogadores for e in equipes)]
    if jogadores_livres:
        print(f"\n{visual.amarelo('Sem equipe')}")
        visual.tabela([_linha_jogador(j) for j in jogadores_livres], CABECALHO_JOGADOR)


def simular_partida():
    print("Time da casa:")
    casa = escolher(equipes, "casa")
    print("Time visitante:")
    visitante = escolher(equipes, "visitante")
    if not casa or not visitante:
        return
    if casa is visitante:
        print("Escolha equipes diferentes.")
        return
    try:
        partida = Partida(casa, visitante)
    except ValueError as erro:
        print(erro)
        return
    partida.simular()
    visual.mostrar_partida(partida)
    partida_id = banco.salvar_partida(partida)
    print(f"\nPartida #{partida_id} salva no banco.")


def ver_historico():
    partidas = banco.historico()
    if not partidas:
        print("Nenhuma partida salva ainda.")
        return
    linhas = [[id_, data, visual.vermelho(casa), f"{g1} x {g2}", visual.azul(visitante)]
              for id_, data, casa, g1, g2, visitante in partidas]
    visual.tabela(linhas, ["#", "Data", "Casa", "Placar", "Visitante"])
    escolha = input("Número da partida para ver estatísticas (Enter para voltar): ")
    if escolha.isdigit():
        estatisticas = banco.estatisticas_da_partida(int(escolha))
        if not estatisticas:
            print("Partida não encontrada.")
            return
        visual.tabela([list(linha) for linha in estatisticas],
                      ["Jogador", "Equipe", "Gols", "Assist.", "Defesas"])


def ver_ranking():
    linhas = banco.ranking()
    if not linhas:
        print("Nenhuma partida salva ainda.")
        return
    visual.tabela([[pos, *linha] for pos, linha in enumerate(linhas, 1)],
                  ["Pos.", "Jogador", "Posição", "Jogos", "Gols", "Assist.", "Defesas"])


MENU = """
===== SIMULADOR DE FUTEBOL 6x6 =====
1. Carregar dados de exemplo
2. Cadastrar jogador
3. Cadastrar treinador
4. Criar equipe
5. Adicionar jogador a uma equipe
6. Listar equipes e jogadores
7. Simular partida
8. Histórico de partidas
9. Ranking geral (banco)
0. Sair
"""
ACOES = {"1": carregar_exemplo, "2": cadastrar_jogador, "3": cadastrar_treinador, "4": criar_equipe,
         "5": adicionar_jogador_equipe, "6": listar_equipes, "7": simular_partida,
         "8": ver_historico, "9": ver_ranking}

if __name__ == "__main__":
    banco.criar_tabelas()
    while True:
        print(visual.ciano(MENU))
        opcao = input("Opção: ")
        if opcao == "0":
            break
        ACOES.get(opcao, lambda: print("Opção inválida."))()