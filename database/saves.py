from database.tabelas import (
    players_db, habilidades_db, itens_db, estados_db,
    players_estados_db, players_habilidades_db, players_itens_db)
from database.conexao import conectar
from contextlib import closing
import sqlite3

def getOuPost_estado(est_nome, conn=None):
    try:
        return estados_db.post_estado(est_nome, conn=conn)
    except sqlite3.IntegrityError:
        estado = estados_db.get_estado_peloNome(est_nome, conn=conn)
        return estado["id"]
    
def getOuPost_habilidade(hab_nome, conn=None):
    try:
        return habilidades_db.post_habilidade(hab_nome, conn=conn)
    except sqlite3.IntegrityError:
        habilidade = habilidades_db.get_habilidade_peloNome(hab_nome, conn=conn)
        return habilidade["id"]

def getOuPost_item(item_nome, conn=None):
    try:
        return itens_db.post_item(item_nome, conn=conn)
    except sqlite3.IntegrityError:
        item = itens_db.get_item_peloNome(item_nome, conn=conn)
        return item["id"]

def salvar_player(player_obj):
    with closing(conectar()) as conn:
        with conn:
            player_id = players_db.post_player(
                nome=player_obj.nome,
                nivel=player_obj.nivel,
                exp_n=player_obj.exp_necessario,
                exp=player_obj.exp,
                mana_m=player_obj.mana_maxima,
                mana=player_obj.mana,
                vida_m=player_obj.vida_maxima,
                vida=player_obj.vida,
                defesa=player_obj.defesa,
                conn=conn
            )
            for est in player_obj.estados:
                estado_id = getOuPost_estado(est, conn=conn)
                players_estados_db.post_player_estado(player_id, estado_id, conn=conn)

            for hab in player_obj.habilidades:
                id_habilidade = getOuPost_habilidade(hab, conn=conn)
                players_habilidades_db.post_player_habilidade(player_id, id_habilidade, conn=conn)

            for item, quantia in player_obj.inventario.items():
                id_item = getOuPost_item(item, conn=conn)
                players_itens_db.post_player_item(player_id, id_item, quantia, conn=conn)

    return player_id