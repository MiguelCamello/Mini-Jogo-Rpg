from utils.carregar_json import carregar_json
from interface.funcoes import descricao_efeito
from utils.erros import EfeitoInexistenteError
from interface.cores import RESET, PRETO, AZUL, ROXO, DOURADO, VERDE, VERMELHO

# =================== #
#  Funções de Barras  #
# =================== #

def barra(maximo=1, atual=1, tamanho=10, cor=RESET):
    proporcao = max(0, min(atual / maximo, 1))
    barra_prenchida = round(proporcao * tamanho)
    barra_vazia = tamanho - barra_prenchida
    return (cor + "▮" * barra_prenchida + "▯" * barra_vazia + "\033[0m")

def barra_exp(maximo=1, atual=1, nivel=1):
    exp = str(atual)+"/"+str(maximo)
    linhas = {
        "l1": f" {VERDE}{" ____":<29}{RESET}",
        "l2": f" {VERDE}{"|    | Experiência":<21}{exp:<8}{RESET}",
        "l3": f" {VERDE}| {nivel:02d} |{RESET}{barra(maximo, atual, 20, VERDE):<32}",
        "l4": f" {VERDE}{"|____|":<29}{RESET}"}
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
        "l2": f"  {AZUL}{"Mana":<10}{mana:<18}{RESET}"}
    return linhas

# ==================== #
#  Funções do Inimigo  #
# ==================== #

def carregar_sprite(inimigo_obj, reset="\033[0m"):
    sprite_raw = inimigo_obj.sprite_dict()
    cor = sprite_raw["cor"]
    sprite = {}
    for chave, valor in sprite_raw.items():
        if chave == "cor":
            continue
        sprite[chave] = cor+valor+reset
    return sprite

def drops(inimigo_obj):
    drops_list = []

    for nome, porcentagem in inimigo_obj.drops.items():
        texto = f"= {nome:<20}{porcentagem:02d}% ="
        drops_list.append(texto)

    return {
        f"l{linha}": texto
        for linha, texto in enumerate(drops_list, start=1)
    }


# =================== #
#  Funções do Player  #
# =================== #

def estados(player_obj):
    efeitos_json = carregar_json(efeitos=True)["efeitos"]
    estado_list = []

    for estado in player_obj.estados:
        if estado.lower() not in efeitos_json:
            raise EfeitoInexistenteError

        estado_list.append(estado)

    if not estado_list:
        return ""
    
    return " ".join(
        f"{efeitos_json[estado.lower()].get('cor', RESET)}[{estado}]{RESET}"
        for estado in estado_list
    )

def habilidades(obj):
    hab_json = obj.habilidades_json

    raridades = {
        "comum": [],
        "raro": [],
        "epico": [],
        "lendario": []
    }

    for habilidade in obj.habilidades:
        dados = hab_json[habilidade]

        efeito = descricao_efeito(dados)

        texto = (
            f"  ==  {dados['nome']:<30}"
            f"{efeito:<15}"
            f"{'Mana: ' + str(dados['custo_mana']):<11}  ==  "
        )

        raridade = dados["raridade"]

        if raridade == "comum":
            texto = PRETO + texto + RESET
        if raridade == "raro":
            texto = AZUL + texto + RESET
        elif raridade == "epico":
            texto = ROXO + texto + RESET
        elif raridade == "lendario":
            texto = DOURADO + texto + RESET

        raridades[raridade].append(texto)

    todas = sum(raridades.values(), [])

    return {
        f"l{i}": texto
        for i, texto in enumerate(todas, start=1)
    }