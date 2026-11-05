from sistemas.criar_classe import criar_player, criar_inimigo
from interface.tela_combate import tela_combate
from interface.tela_habilidades import tela_habilidades
from interface.funcoes import limpar_terminal

inimigo = criar_inimigo("goblin")
player = criar_player("Miguel Camellot", estados=["Fortalecido", "Envenenado"], mana=10, habilidades=["soco_fraco","soco_pesado", "golpe_vampirico", "julgamento_divino", "golpe_absoluto"])


#tela_combate(player, inimigo)
while inimigo.vivo and player.vivo:
    tela_combate(player_obj=player, inimigo_obj=inimigo)
    oi = input("ação > ").lower().strip()
    limpar_terminal()
    if oi in "habilidades":
        tela_habilidades(player)
        input(">")
        limpar_terminal()
