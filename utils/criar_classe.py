from utils.carregar_json import carregar_json
from model.inimigo import Inimigo
from model.player import Player


def criar_inimigo(nome):
    dados = carregar_json(inimigo=True, habilidades=True)
    return Inimigo(
        inimigo_json=dados["inimigos"][nome],
        habilidades_json=dados["habilidades"]
        )

def criar_player(nome, **resto):
    dados = carregar_json(habilidades=True)["habilidades"]
    return Player(
        nome=nome,
        habilidades_json=dados,
        **resto
    )  # função perigossisima, pode retornar erro se eu fizer merda
