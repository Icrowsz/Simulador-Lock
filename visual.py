"""Parte visual do terminal: cores (colorama), tabelas (tabulate) e animação."""
import time
from colorama import init, Fore, Style
from tabulate import tabulate

init(autoreset=True)

PAUSA = 0.4  # segundos entre as linhas da narração


def _cor(cor, texto):
    return f"{cor}{texto}{Style.RESET_ALL}"


def vermelho(texto):
    return _cor(Style.BRIGHT + Fore.RED, texto)


def azul(texto):
    return _cor(Style.BRIGHT + Fore.BLUE, texto)


def verde(texto):
    return _cor(Style.BRIGHT + Fore.GREEN, texto)


def ciano(texto):
    return _cor(Fore.CYAN, texto)


def amarelo(texto):
    return _cor(Style.BRIGHT + Fore.YELLOW, texto)


def tabela(linhas, cabecalhos):
    print(tabulate(linhas, headers=cabecalhos, tablefmt="fancy_grid"))


def placar_colorido(partida):
    """Casa em vermelho, visitante em azul."""
    g_casa, g_vis = partida.placar()
    return f"{vermelho(f'{partida.casa.nome} {g_casa}')} x {azul(f'{g_vis} {partida.visitante.nome}')}"


def cor_da_equipe(partida, nome_equipe):
    return vermelho(nome_equipe) if nome_equipe == partida.casa.nome else azul(nome_equipe)


def mostrar_partida(partida):
    """Mostra a narração linha a linha, com pausa, e depois o resumo."""
    print(f"\n{vermelho(partida.casa.nome)} vs {azul(partida.visitante.nome)}")
    print(amarelo("Apito inicial! A bola rola...\n"))
    time.sleep(PAUSA)
    for texto, destaque in partida.eventos:
        print(verde(texto) if destaque else texto)
        time.sleep(PAUSA)

    print(f"\n{amarelo('FIM DE JOGO')}")
    print(f"  {placar_colorido(partida)}\n")
    linhas = [[j.nome, cor_da_equipe(partida, eq.nome), est.gols, est.assistencias, est.defesas]
              for eq, j, est in partida.estatisticas()]
    tabela(linhas, ["Jogador", "Equipe", "Gols", "Assist.", "Defesas"])
