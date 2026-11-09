from pathlib import Path
import json

BASE_DIR = Path(__file__).parent.parent
INIMIGOS_JSON = BASE_DIR / "data" / "inimigos.json"
HABILIDADES_JSON = BASE_DIR / "data" / "habilidades.json"
EFEITOS_JSON = BASE_DIR / "data" / "efeitos.json"
ITENS_JSON = BASE_DIR / "data" / "itens.json"
SPRITES_JSON = BASE_DIR / "data" / "sprites.json"
CORES_JSON = BASE_DIR / "data" / "cores.json"

def carregar_json(
        inimigo=False,
        habilidades=False,
        efeitos=False,
        itens=False,
        sprites=False,
        cores=False
        ):
    
    dados={}

    if inimigo:
        with open(INIMIGOS_JSON, "r", encoding="utf-8") as inimigos:
            dados["inimigos"] = json.load(inimigos)
    if habilidades:
        with open(HABILIDADES_JSON, "r", encoding="utf-8") as habilidades:
            dados["habilidades"] = json.load(habilidades)
    if efeitos:
        with open(EFEITOS_JSON, "r", encoding="utf-8") as efeitos:
            dados["efeitos"] = json.load(efeitos)
    if itens:
        with open(ITENS_JSON, "r", encoding="utf-8") as itens:
            dados["itens"] = json.load(itens)
    if sprites:
        with open(SPRITES_JSON, "r", encoding="utf-8") as sprites:
            dados["sprites"] = json.load(sprites)
    if cores:
         with open(CORES_JSON, "r", encoding="utf-8") as cores:
            dados["cores"] = json.load(cores)

    return dados