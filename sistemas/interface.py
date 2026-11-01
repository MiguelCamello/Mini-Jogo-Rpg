from utils.carregar_json import carregar_json
from utils.erros import EfeitoInexistenteError
from wcwidth import wcswidth
import re

VERMELHO = "\033[91m"
DOURADO = "\033[33m"
VERDE = "\033[92m"
AZUL = "\033[94m"
FUNDO_CINZA = "\033[100m"
RESET = "\033[0m"

    

def centralizar(texto, largura):
    texto_limpo = re.sub(r'\033\[[0-9;]*m', '', texto)
    espacos = largura - wcswidth(texto_limpo)

    esquerda = espacos // 2
    direita = espacos - esquerda

    return " " * esquerda + texto + " " * direita

def estados(obj):
    efeitos_json = carregar_json(efeitos=True)["efeitos"]
    estadoList=[]
    estados_text=""
    for estado in obj.estados:
        if estado.lower() not in efeitos_json:
            raise EfeitoInexistenteError
        if estado in ["Vivo", "Morto-vivo"]:
            continue
        if estado == "morto":
            estadoList.append(estado)
            break
        estadoList.append(estado)
    if not estadoList:
        return ""
    for estado in estadoList:
        cor = efeitos_json[estado.lower()].get("cor", RESET)
        estados_text += f"{cor}[{estado}]{RESET} "
        estados_text + RESET
    return estados_text.rstrip()

#===================#
# Funções de Barras #
#===================#

def barra(max=1, atual=1, tamanho=10, cor=RESET):
    barra_prench = round((atual/max) * tamanho)
    barra_vazia = tamanho - barra_prench
    barra = cor + "▮" * barra_prench + "▯" * barra_vazia + "\033[0m"
    return barra

def barra_exp(maximo=1, atual=1, nivel=1):
    exp = str(atual)+"/"+str(maximo)
    linhas = {
    "l1": f" {VERDE}{" ____":<29}{RESET}",
    "l2": f" {VERDE}{"|    | Experiência":<21}{exp:<8}{RESET}",
    "l3": f" {VERDE}| {nivel:02d} |{RESET}{barra(maximo,atual,20,VERDE):<32}",
    "l4": f" {VERDE}{"|____|":<29}{RESET}" }
    return linhas

def barra_vida(maximo=1, atual=1, defesa=10):
    vida = str(atual)+"/"+str(maximo)
    linhas = {
    "l1": f"  {VERMELHO}{"Vida"}{vida:>14}{DOURADO} {"Def"} {defesa:<5}{RESET}",
    "l2": f" {barra(maximo, atual, 19, cor=VERMELHO)+barra(tamanho=7, cor=DOURADO)}   "}
    return linhas

def barra_mana(maximo=1, atual=1):
    mana = str(atual)+"/"+str(maximo)
    linhas = {
    "l1": f" {barra(maximo, atual, 16, cor=AZUL)} {" "*12}",
    "l2": f"  {AZUL}{"Mana":<10}{mana:<18}{RESET}" }
    return linhas

#====================#
# Funções do Inimigo #
#====================#

def carregar_sprite(inimigo_obj, reset="\033[0m"):
    sprite_raw = inimigo_obj.sprite_dict()
    cor = sprite_raw["cor"]
    sprite = {}
    for chave, valor in sprite_raw.items():
        if chave == "cor":
            continue
        sprite[chave] = cor+valor+reset
    return sprite

chao_cinza = {
    "l1": FUNDO_CINZA+(" "*17)+RESET,
    "l2": FUNDO_CINZA+(" "*12)+RESET
    }

#===========#
# principal #
#===========#

def tela_principal(player_obj, inimigo_obj):
    linha, espaco = f"|{"="*92}|", f"|{" "*92}|"
    #player barra
    ExpPlayer = barra_exp(
        atual=player_obj.exp,
        maximo=player_obj.exp_necessario,
        nivel=player_obj.nivel)
    VidaPlayer = barra_vida(
        atual=player_obj.vida,
        maximo=player_obj.vida_maxima,
        defesa=player_obj.defesa
    )
    ManaPlayer = barra_mana(
        atual=player_obj.mana,
        maximo=player_obj.mana_maxima
    )
    #inimigo barra
    VidaInimigo = barra_vida(
        atual=inimigo_obj.vida,
        maximo=inimigo_obj.vida_maxima,
        defesa=inimigo_obj.defesa
    )
    ManaInimigo = barra_mana(
        atual=inimigo_obj.mana,
        maximo=inimigo_obj.mana_maxima
    )

    sprite = carregar_sprite(inimigo_obj)
    nome_player = "⭐ == "+player_obj.nome+" == ⭐"
    nome_inimigo = "== " + inimigo_obj.nome + " =="

    print(f"""
{linha}
|{"RPG PIKISSIMO":^92}|
{linha}
{espaco}
{espaco}
|{nome_player:^28} {" "*30} {nome_inimigo:^30}|
{espaco}
| {estados(player_obj):^30} {" "*32} {estados(inimigo_obj):^30} |
{espaco}
|{ ExpPlayer["l1"]}{" "*6}{centralizar(sprite.get("l1", ""),26)}{VidaInimigo["l1"]}|
|{ ExpPlayer["l2"]}{" "*6}{centralizar(sprite.get("l2", ""),26)}{VidaInimigo["l2"]}|
|{ ExpPlayer["l3"]}{" "*6}{centralizar(sprite.get("l3", ""),26)}{" "*30}|
|{ ExpPlayer["l4"]}{" "*6}{centralizar(sprite.get("l4", ""),26)}{ManaInimigo["l1"]}|
|{          " "*30}{" "*6}{centralizar(sprite.get("l5", ""),26)}{ManaInimigo["l2"]}|
|{VidaPlayer["l1"]}{" "*6}{centralizar(chao_cinza['l1'],26)}{" "*30}|
|{VidaPlayer["l2"]}{" "*6}{centralizar(chao_cinza['l2'],26)}{" "*30}|
|{          " "*30} {                              " "*30} {" "*30}|
|{ManaPlayer["l1"]} {                              " "*30} {" "*30}|
|{ManaPlayer["l2"]} {                              " "*30} {" "*30}|
{espaco}
{espaco}
|{" "*15}|{"="*60}|{" "*15}|
|{" "*15}|{"AÇÕES":^60}|{" "*15}|
|{" "*15}|   {"_"*18} {"_"*16} {"_"*18}   |{" "*15}|
|{" "*15}|  |{" "*18}|{" "*16}|{" "*18}|  |{" "*15}|
|{" "*15}|  |{"HABILIDADES":^18}|{"USAR ITENS":^16}|{"DESCANSAR":^18}|  |{" "*15}|
|{" "*15}|  |{"_"*18}|{"_"*16}|{"_"*18}|  |{" "*15}|
|{" "*15}|{" "*60}|{" "*15}|
{linha}
""")

