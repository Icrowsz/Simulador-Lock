"""Quem faz o quê em campo.

Cada tipo de lance tem posições PRINCIPAIS (fazem bem e com mais frequência) e
SECUNDÁRIAS (também podem fazer, mas com menos frequência e menos chance de sucesso).
"""
import random

PAPEIS = {
    "construir": {"principal": ("Meio-campista", "Ala"), "secundaria": ("Atacante", "Zagueiro")},
    "finalizar": {"principal": ("Atacante",), "secundaria": ("Meio-campista", "Ala")},
    "defender": {"principal": ("Zagueiro",), "secundaria": ("Meio-campista", "Ala")},
}

PENALIDADE_SECUNDARIA = 0.75  # atributo x 0,75 quando o jogador faz um lance que não é o da sua posição
PESO_PRINCIPAL = 4            # chance relativa de ser sorteado para o lance
PESO_SECUNDARIO = 1


def fator(jogador, papel):
    """Multiplicador do atributo: 1,0 na posição original, menor fora dela."""
    if jogador.posicao in PAPEIS[papel]["principal"]:
        return 1.0
    return PENALIDADE_SECUNDARIA


def escolher(jogadores, papel, excluir=None):
    """Sorteia quem faz o lance. O goleiro só entra na defesa final do chute (não é sorteado aqui)."""
    campo = [j for j in jogadores if j.posicao != "Goleiro" and j is not excluir]
    principais = PAPEIS[papel]["principal"]
    secundarias = PAPEIS[papel]["secundaria"]
    candidatos = [j for j in campo if j.posicao in principais + secundarias] or campo
    pesos = [PESO_PRINCIPAL if j.posicao in principais else PESO_SECUNDARIO for j in candidatos]
    return random.choices(candidatos, weights=pesos)[0]
