def verificar_resposta(variavel):
    if variavel in ["sim", "ss", "s"]:
        return True
    elif variavel in ["nao", "nn", "n"]:
        return False
    else:
        return False