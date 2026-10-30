from database.tabelas import (
    players_db, habilidades_db, itens_db, estados_db,
    players_estados_db, players_habilidades_db, players_itens_db)
from sistemas.criar_classe import criar_player
from database.conexao import conectar
from contextlib import closing
import sqlite3


def getOrCreate_estado(est_nome, conn=None):
    try:
        return estados_db.create(est_nome, conn=conn)
    except sqlite3.IntegrityError:
        estado = estados_db.find_by_name(est_nome, conn=conn)
        return estado["id"]


def getOrCreate_habilidade(hab_nome, conn=None):
    try:
        return habilidades_db.create(hab_nome, conn=conn)
    except sqlite3.IntegrityError:
        habilidade = habilidades_db.find_by_name(
            hab_nome, conn=conn)
        return habilidade["id"]


def getOrCreate_item(item_nome, conn=None):
    try:
        return itens_db.create(item_nome, conn=conn)
    except sqlite3.IntegrityError:
        item = itens_db.find_by_name(item_nome, conn=conn)
        return item["id"]


def buscar_estados(player_id, conn=None):
    playerEstList = []
    playerEstDados = players_estados_db.find_by_playerId(player_id, conn=conn)
    for dado in playerEstDados:
        estado = estados_db.get(dado["estado_id"], conn=conn)
        playerEstList.append(estado["nome"])
    return playerEstList

def buscar_habilidades(player_id, conn=None):
    playerHabList = []
    playerHabDados = players_habilidades_db.find_by_playerId(player_id, conn=conn)
    for dado in playerHabDados:
        habilidade = habilidades_db.get(dado["habilidade_id"], conn=conn)
        playerHabList.append(habilidade["nome"])
    return playerHabList

def buscar_itens(player_id, conn=None):
    playerItensDict = {}
    playerItensDados = players_itens_db.find_by_playerId(player_id, conn=conn)
    for dado in playerItensDados:
        item = itens_db.get(dado["item_id"], conn=conn)
        quantia = dado["quantidade"]
        playerItensDict[item["nome"]] = quantia
    return playerItensDict
        
def salvar_player(player_obj):
    with closing(conectar()) as conn:
        with conn:
            player_id = players_db.create(
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
                estado_id = getOrCreate_estado(est, conn=conn)
                players_estados_db.create(
                    player_id, estado_id, conn=conn)

            for hab in player_obj.habilidades:
                id_habilidade = getOrCreate_habilidade(hab, conn=conn)
                players_habilidades_db.create(
                    player_id, id_habilidade, conn=conn)

            for item, quantia in player_obj.inventario.items():
                id_item = getOrCreate_item(item, conn=conn)
                players_itens_db.create(
                    player_id, id_item, quantia, conn=conn)

            print(f"Dados de {player_obj.nome} salvo com sucesso!")
    return player_id


def carregar_player(player_id):
    with closing(conectar()) as conn:
        with conn:
            player_dados = players_db.get(player_id, conn=conn)
            estados = buscar_estados(player_id, conn=conn)
            habilidades = buscar_habilidades(player_id, conn=conn)
            itens = buscar_itens(player_id, conn=conn)

            return criar_player(
                nome=player_dados["nome"],
                estados=estados,
                nivel=player_dados["nivel"],
                exp_necessario=player_dados["exp_necessario"],
                exp=player_dados["exp"],
                mana_maxima=player_dados["mana_maxima"],
                mana=player_dados["mana"],
                vida_maxima=player_dados["vida_maxima"],
                vida=player_dados["vida"],
                defesa=player_dados["defesa"],
                itens=itens,
                habilidades=habilidades
            )

def atualizar_player(player_id, player_obj, conn=None):
    with closing(conectar()) as conn:
        with conn:
            players_db.update(
                id=player_id,
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

            #deleta as relações m:m daquele player e cria novas no lugar
            players_estados_db.delete_by_playerId(player_id, conn=conn)
            for est in player_obj.estados:
                estado_id = getOrCreate_estado(est, conn=conn)
                players_estados_db.create(
                    player_id, estado_id, conn=conn)
            
            players_habilidades_db.delete_by_playerId(player_id, conn=conn)
            for hab in player_obj.habilidades:
                id_habilidade = getOrCreate_habilidade(hab, conn=conn)
                players_habilidades_db.create(
                    player_id, id_habilidade, conn=conn)
            
            players_itens_db.delete_by_playerId(player_id, conn=conn)
            for item, quantia in player_obj.inventario.items():
                id_item = getOrCreate_item(item, conn=conn)
                players_itens_db.create(
                    player_id, id_item, quantia, conn=conn)

def deleter_player(player_id):
    players_db.delete(player_id)
    # o sql se encarrega de deletar as tabelas m:m
    # usando o ON DELETE CASCADE

def listar_players():
    linha = "+"+"-"*46+"+"
    players_dados = players_db.get_all()
    for player in players_dados:
        print(f"""
{linha}
|{f"FICHA DO PLAYER Id:{player["id"]}":^46}|
{linha}
| Nome: {player["nome"]:<39}|
| Nivel: {player["nivel"]:<38}|
{linha}
|{"ATRIBUTOS":<46}|
| Vida: {str(player["vida_maxima"])+"/"+str(player["vida"]):<39}|
| Mana: {str(player["mana_maxima"])+"/"+str(player["mana"]):<39}|
| Defesa: {player["defesa"]:<37}|
| Experiência: {str(player["exp_necessario"])+"/"+str(player["exp"]):<32}|
{linha}
""")

