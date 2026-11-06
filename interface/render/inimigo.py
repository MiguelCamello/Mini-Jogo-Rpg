def sprite_dict(inimigo_obj, reset="\033[0m"):
    sprite_raw = inimigo_obj.sprite_dict()
    cor = sprite_raw["cor"]
    sprite = {}
    for chave, valor in sprite_raw.items():
        if chave == "cor":
            continue
        sprite[chave] = cor+valor+reset
    return sprite


def drops_dict(inimigo_obj):
    drops_list = []

    for nome, porcentagem in inimigo_obj.drops.items():
        texto = f"= {nome:<20}{porcentagem:02d}% ="
        drops_list.append(texto)

    return {
        f"l{linha}": texto
        for linha, texto in enumerate(drops_list, start=1)
    }