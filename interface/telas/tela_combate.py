from interface.render.barras import barra_exp, barra_mana, barra_vida
from interface.render.inimigo import sprite_dict, drops_dict
from interface.render.player import formatar_estados

from interface.cores import RESET, DOURADO, PRETO, FUNDO_CINZA
from interface.funcoes import centralizar

chao_cinza = {
    "l1": FUNDO_CINZA+(" "*17)+RESET,
    "l2": FUNDO_CINZA+(" "*12)+RESET
}

def tela_combate(player_obj, inimigo_obj):
    # player barra
    Exp_Player = barra_exp(
        atual=player_obj.exp,
        maximo=player_obj.exp_necessario,
        nivel=player_obj.nivel)
    
    Vida_Player = barra_vida(
        atual=player_obj.vida,
        maximo=player_obj.vida_maxima,
        defesa=player_obj.defesa)
    
    Mana_Player = barra_mana(
        atual=player_obj.mana,
        maximo=player_obj.mana_maxima)
    
    # inimigo barra
    Vida_Inimigo = barra_vida(
        atual=inimigo_obj.vida,
        maximo=inimigo_obj.vida_maxima,
        defesa=inimigo_obj.defesa)
    
    Mana_Inimigo = barra_mana(
        atual=inimigo_obj.mana,
        maximo=inimigo_obj.mana_maxima)
    
    Drops_Inimigos = drops_dict(inimigo_obj)

    sprite = sprite_dict(inimigo_obj)

    nome_player = "⭐ == "+player_obj.nome+" == ⭐"
    nome_inimigo = "== " + inimigo_obj.nome + " =="

    linha, espaco = f"|{"="*92}|", f"|{" "*92}|"

    print(f"""
{linha}
|{"== MEU RPG ==":^92}|
{linha}
{espaco}
{espaco}
|{DOURADO}{nome_player:^28} {" "*30} {PRETO}{nome_inimigo:^30}{RESET}|
{espaco}
| {formatar_estados(player_obj.estados):^30} {" "*32} {formatar_estados(inimigo_obj.estados):^30} |
{espaco}
|{Exp_Player["l1"]} {" "*4}{centralizar(sprite.get("l1", ""), 26)} {Vida_Inimigo["l1"]}|
|{Exp_Player["l2"]} {" "*4}{centralizar(sprite.get("l2", ""), 26)} {Vida_Inimigo["l2"]}|
|{Exp_Player["l3"]} {" "*4}{centralizar(sprite.get("l3", ""), 26)} {" "*30}|
|{Exp_Player["l4"]} {" "*4}{centralizar(sprite.get("l4", ""), 26)} {Mana_Inimigo["l1"]}|
|{" "*30} {" "*4}{centralizar(sprite.get("l5", ""), 26)} {Mana_Inimigo["l2"]}|
|{Vida_Player["l1"]} {" "*4}{centralizar(chao_cinza["l1"], 26)} {" "*30}|
|{Vida_Player["l2"]} {" "*4}{centralizar(chao_cinza["l2"], 26)} {PRETO} {"="*10} Drops {"="*10} {RESET} |
|{" "*30} {" "*30} {PRETO}{(Drops_Inimigos.get("l2", "")):^30}{RESET}|
|{Mana_Player["l1"]} {" "*30} {PRETO}{(Drops_Inimigos.get("l2", "")):^30}{RESET}|
|{Mana_Player["l2"]} {" "*30} {PRETO}{(Drops_Inimigos.get("l3", "")):^30}{RESET}|
|{" "*30} {" "*30} {PRETO}{(Drops_Inimigos.get("l4", "")):^30}{RESET}|
{espaco}
{espaco}
|{" "*15}|{"="*60}|{" "*15}|
|{" "*15}|{"AÇÕES":^60}|{" "*15}|
|{" "*15}|   {"_"*18} {"_"*16} {"_"*18}   |{" "*15}|
|{" "*15}|  |{" "*18}|{" "*16}|{" "*18}|  |{" "*15}|
|{" "*15}|  |{"HABILIDADES":^18}|{"ITENS":^16}|{"DESCANSAR":^18}|  |{" "*15}|
|{" "*15}|  |{"_"*18}|{"_"*16}|{"_"*18}|  |{" "*15}|
|{" "*15}|{" "*60}|{" "*15}|
{linha}
""")
