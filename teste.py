from sistemas.interface import tela_principal
from sistemas.criar_classe import criar_player, criar_inimigo

inimigo = criar_inimigo("goblin")
player = criar_player("Miguel Camellot", estados=["Fortalecido", "Envenenado"])

tela_principal(player, inimigo)
