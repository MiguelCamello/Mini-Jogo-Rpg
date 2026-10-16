from model.inimigo import Inimigo
from utils.carregar_json import carregar_json

def criar_inimigo(nome):
    dados = carregar_json(inimigo=True)
    return Inimigo(dados["inimigos"][nome])