from interface.render.barras import barra
from model.cores import cores_obj as c_obj
from interface.formatação import centralizar


def card_render(save):
    exp = str(save['exp'])+"/"+str(save['exp_necessario'])
    vida = str(save['vida'])+"/"+str(save['vida_maxima'])
    mana = str(save['mana'])+"/"+str(save['mana_maxima'])

    return [
        # exp
        centralizar(f"{c_obj.VERDE}{" ____":<21}{c_obj.RESET}", 24),
        centralizar(f"{c_obj.VERDE}{"|    | Exp":<13}{exp:>8}{c_obj.RESET}", 24),
        centralizar(f"{c_obj.VERDE}| {save['nivel']:02d} |{c_obj.RESET}{barra(save['exp_necessario'], save['exp'], 15, c_obj.VERDE):<24}", 24),
        centralizar(f"{c_obj.VERDE}{"|____|":<21}{c_obj.RESET}", 24),

        #vida
        centralizar(f" {c_obj.VERMELHO}{"Vida"}{vida:>10}{c_obj.DOURADO} {"Def"} {save['defesa']}{c_obj.RESET}", 24),
        centralizar(f"{barra(save['vida_maxima'], save['vida'], 15, cor=c_obj.VERMELHO)+barra(tamanho=6, cor=c_obj.DOURADO)}", 24),

        #mana
        centralizar(f"{barra(save['mana_maxima'], save['mana'], 18, cor=c_obj.AZUL)}", 24),
        centralizar(f" {c_obj.AZUL}{"Mana"}   {mana:>10}{c_obj.RESET}", 24)
    ]
def card_vazio():
    espaco, linha = " "*24, "_"*24
    mais = [
        f"{"     █     ":^24}",
        f"{"     █     ":^24}", 
        f"{"     █     ":^24}", 
        f"{"     █     ":^24}", 
        f"{"█████████████":^24}",
        f"{"     █     ":^24}",
        f"{"     █     ":^24}",
        f"{"     █     ":^24}",
        f"{"     █     ":^24}",
        f"{"":^24}",
        f"{"":^24}",
        f"{"NOVA JORNADA":^24}",
    ]

    card = []

    card.append(f"{c_obj.PRETO2}{linha:^30}{c_obj.RESET}")

    for _ in range(3):
        card.append(f"{c_obj.PRETO2}{"|"+espaco+"|":^30}{c_obj.RESET}")
    for i in range(12):
        card.append(f"{c_obj.PRETO2}{"|"+mais[i]+"|":^30}{c_obj.RESET}")
    for _ in range(2):
        card.append(f"{c_obj.PRETO2}{"|"+espaco+"|":^30}{c_obj.RESET}")

    card.append(f"{c_obj.PRETO2}{("|"+linha+"|"):^30}{c_obj.RESET}")

    return card

def card_save(save):
    nome = centralizar(f"{c_obj.DOURADO}{("--== " + save['nome'] + " ==--"):^24}{c_obj.RESET}",24)
    espaco, linha = " "*24, "_"*24
    linhas = card_render(save)

    return [
        f"{linha:^30}",
        f"{("|"+(espaco)+"|"):^30}",
        f"{("|"+(espaco)+"|"):^30}",
        f"{centralizar("|"+nome+"|", 30)}",
        f"{("|"+(espaco)+"|"):^30}",
        f"{centralizar("|"+ linhas[0] +"|", 30)}",
        f"{centralizar("|"+ linhas[1] +"|", 30)}",
        f"{centralizar("|"+ linhas[2] +"|", 30)}",
        f"{centralizar("|"+ linhas[3] +"|", 30)}",
        f"{("|"+(espaco)+"|"):^30}",
        f"{("|"+(espaco)+"|"):^30}",
        f"{centralizar("|"+ linhas[4] +"|", 30)}",
        f"{centralizar("|"+ linhas[5] +"|", 30)}",
        f"{("|"+(espaco)+"|"):^30}",
        f"{centralizar("|"+ linhas[6] +"|", 30)}",
        f"{centralizar("|"+ linhas[7] +"|", 30)}",
        f"{("|"+(espaco)+"|"):^30}",
        f"{("|"+(espaco)+"|"):^30}",
        f"{("|"+linha+"|"):^30}",
    ]


def tela_saves(sqliteRow):
    linha, espaco = f"|{"="*92}|", f"|{" "*92}|"
    

    card1 = card_vazio()
    card2 = card_vazio()
    card3 = card_vazio()

    if len(sqliteRow) >= 1:
        card1 = card_save(sqliteRow[0])
    if len(sqliteRow) >= 2:
        card2 = card_save(sqliteRow[1])
    if len(sqliteRow) >= 3:
        card3 = card_save(sqliteRow[2])
    
    print(f"""
{linha}
|{"== SAVES ==":^92}|
{linha}
{espaco}
| {"Save 1":^30}{"Save 2":^30}{"Save 3":^30} |""")
    
    for c1, c2, c3 in zip(card1, card2, card3):
        print(f"| {c1}{c2}{c3} |")

    print(f"""|{c_obj.VERMELHO}{"__________________":^30} {c_obj.VERDE}{"_______________":^30} {c_obj.DOURADO}{"_________________":^30}{c_obj.RESET}|
|{c_obj.VERMELHO}{"|                  |":^30} {c_obj.VERDE}{"|               |":^30} {c_obj.DOURADO}{"|                 |":^30}{c_obj.RESET}|
|{c_obj.VERMELHO}{"|   DELETAR SAVE   |":^30} {c_obj.VERDE}{"|   NOVO SAVE   |":^30} {c_obj.DOURADO}{"|  CARREGAR SAVE  |":^30}{c_obj.RESET}|
|{c_obj.VERMELHO}{"|__________________|":^30} {c_obj.VERDE}{"|_______________|":^30} {c_obj.DOURADO}{"|_________________|":^30}{c_obj.RESET}|
{espaco}
{linha}
""")