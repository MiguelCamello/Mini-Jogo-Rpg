from model.cores import cores_obj as c_obj


def barra(maximo=1, atual=1, tamanho=10, cor=c_obj.RESET):
    proporcao = max(0, min(atual / maximo, 1))
    barra_prenchida = round(proporcao * tamanho)
    barra_vazia = tamanho - barra_prenchida
    return (cor + "▮" * barra_prenchida + "▯" * barra_vazia + "\033[0m")


def barra_exp(maximo=1, atual=1, nivel=1):
    exp = str(atual)+"/"+str(maximo)
    linhas = {
        "l1": f" {c_obj.VERDE}{" ____":<29}{c_obj.RESET}",
        "l2": f" {c_obj.VERDE}{"|    | Experiência":<21}{exp:<8}{c_obj.RESET}",
        "l3": f" {c_obj.VERDE}| {nivel:02d} |{c_obj.RESET}{barra(maximo, atual, 20, c_obj.VERDE):<32}",
        "l4": f" {c_obj.VERDE}{"|____|":<29}{c_obj.RESET}"}
    return linhas


def barra_vida(maximo=1, atual=1, defesa=10):
    vida = str(atual)+"/"+str(maximo)
    linhas = {
        "l1": f"  {c_obj.VERMELHO}{"Vida"}{vida:>14}{c_obj.DOURADO} {"Def"} {defesa:<5}{c_obj.RESET}",
        "l2": f" {barra(maximo, atual, 19, cor=c_obj.VERMELHO)+barra(tamanho=7, cor=c_obj.DOURADO)}   "}
    return linhas


def barra_mana(maximo=1, atual=1):
    mana = str(atual)+"/"+str(maximo)
    linhas = {
        "l1": f" {barra(maximo, atual, 16, cor=c_obj.AZUL)} {" "*12}",
        "l2": f"  {c_obj.AZUL}{"Mana"} {mana:>10}{c_obj.RESET}{" "*13}"}
    return linhas
