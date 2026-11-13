import os
import sqlite3
from datetime import datetime

ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "futebol.db")


def _conectar():
    conexao = sqlite3.connect(ARQUIVO)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def criar_tabelas():
    conexao = _conectar()
    conexao.executescript("""
        CREATE TABLE IF NOT EXISTS jogador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            idade INTEGER,
            posicao TEXT NOT NULL,
            chute INTEGER, passe INTEGER, velocidade INTEGER, defesa INTEGER
        );
        CREATE TABLE IF NOT EXISTS partida (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            equipe_casa TEXT NOT NULL,
            equipe_visitante TEXT NOT NULL,
            gols_casa INTEGER NOT NULL,
            gols_visitante INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS estatistica (
            partida_id INTEGER NOT NULL REFERENCES partida(id),
            jogador_id INTEGER NOT NULL REFERENCES jogador(id),
            equipe TEXT NOT NULL,
            gols INTEGER NOT NULL,
            assistencias INTEGER NOT NULL,
            defesas INTEGER NOT NULL,
            PRIMARY KEY (partida_id, jogador_id)
        );
    """)
    conexao.commit()
    conexao.close()


def salvar_partida(partida):
    """Grava a partida e as estatísticas de cada jogador. Devolve o id da partida."""
    g_casa, g_vis = partida.placar()
    conexao = _conectar()
    try:
        cursor = conexao.execute(
            "INSERT INTO partida (data, equipe_casa, equipe_visitante, gols_casa, gols_visitante) "
            "VALUES (?, ?, ?, ?, ?)",
            (datetime.now().strftime("%d/%m/%Y %H:%M"), partida.casa.nome,
             partida.visitante.nome, g_casa, g_vis))
        partida_id = cursor.lastrowid
        for equipe, j, est in partida.estatisticas():
            # se o jogador já existe (mesmo nome), atualiza os dados dele
            conexao.execute(
                "INSERT INTO jogador (nome, idade, posicao, chute, passe, velocidade, defesa) "
                "VALUES (?, ?, ?, ?, ?, ?, ?) "
                "ON CONFLICT(nome) DO UPDATE SET idade=excluded.idade, posicao=excluded.posicao, "
                "chute=excluded.chute, passe=excluded.passe, velocidade=excluded.velocidade, "
                "defesa=excluded.defesa",
                (j.nome, j.idade, j.posicao, j.chute, j.passe, j.velocidade, j.defesa))
            jogador_id = conexao.execute("SELECT id FROM jogador WHERE nome = ?", (j.nome,)).fetchone()[0]
            conexao.execute(
                "INSERT INTO estatistica (partida_id, jogador_id, equipe, gols, assistencias, defesas) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (partida_id, jogador_id, equipe.nome, est.gols, est.assistencias, est.defesas))
        conexao.commit()
        return partida_id
    finally:
        conexao.close()


def _consultar(sql, parametros=()):
    conexao = _conectar()
    try:
        return conexao.execute(sql, parametros).fetchall()
    finally:
        conexao.close()


def historico():
    return _consultar("SELECT id, data, equipe_casa, gols_casa, gols_visitante, equipe_visitante "
                      "FROM partida ORDER BY id DESC")


def estatisticas_da_partida(partida_id):
    return _consultar(
        "SELECT j.nome, e.equipe, e.gols, e.assistencias, e.defesas "
        "FROM estatistica e JOIN jogador j ON j.id = e.jogador_id "
        "WHERE e.partida_id = ? ORDER BY e.equipe, j.nome", (partida_id,))


def ranking():
    return _consultar(
        "SELECT j.nome, j.posicao, COUNT(*) AS jogos, SUM(e.gols), SUM(e.assistencias), SUM(e.defesas) "
        "FROM estatistica e JOIN jogador j ON j.id = e.jogador_id "
        "GROUP BY j.id ORDER BY SUM(e.gols) DESC, SUM(e.assistencias) DESC, SUM(e.defesas) DESC")
