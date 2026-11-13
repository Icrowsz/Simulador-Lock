import random


def chance_ataque(ataque, defesa):
    """Chance de quem ataca vencer o duelo: 90 x 90 = 50%, 70 x 80 = 46,67%."""
    total = ataque + defesa
    if total == 0:
        return 0.5
    return ataque / total


def vence(ataque, defesa):
    return random.random() < chance_ataque(ataque, defesa)
