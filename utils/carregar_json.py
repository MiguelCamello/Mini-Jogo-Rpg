from pathlib import Path
import json

BASE_DIR = Path(__file__).parent.parent
INIMIGOS_JSON = BASE_DIR / "data" / "inimigos.json"
HABILIDADES_JSON = BASE_DIR / "data" / "habilidades.json"
EFEITOS_JSON = BASE_DIR / "data" / "efeitos.json"

def carregar_json(inimigo=False, habilidades=False, efeitos=False):
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

    return dados

