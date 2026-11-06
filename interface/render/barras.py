from interface.cores import RESET, AZUL, VERDE, VERMELHO, DOURADO

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
        "l2": f"  {AZUL}{"Mana"} {mana:>10}{RESET}{" "*13}"}
    return linhas