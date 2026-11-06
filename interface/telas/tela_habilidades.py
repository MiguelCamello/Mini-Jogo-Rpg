from interface.cores import RESET, PRETO, AZUL, ROXO, DOURADO, VERMELHO
from interface.render.player import habilidades_list
from interface.funcoes import centralizar


def tela_habilidades(player_obj):
    hab_dict = habilidades_list(player_obj)
    
    linha, espaco = f"|{"="*72}|", f"|{" "*72}|"

    print(f"""
{" "*10}{linha}
{" "*10}|{"Mana atual:":>12} {AZUL}{player_obj.mana:<6}{RESET} {"== HABILIDADES ==":<18} {PRETO}Comum {AZUL}Raro {ROXO}Épico {DOURADO}Lendário {VERMELHO}Mítico {RESET}|
{" "*10}{linha}
{" "*10}{espaco}
{" "*10}|{" "*5}{'== Nome ==':<28}{'== Efeito ==':<18}{'== Custo Mana ==':<21}|
{" "*10}{espaco}
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l1", ""), 70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l2", ""), 70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l3", ""), 70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l4", ""), 70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l5", ""), 70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l6", ""), 70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l7", ""), 70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l8", ""), 70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l9", ""), 70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l10", ""), 70)} |
{" "*10}{espaco}
{" "*10}{espaco}
{" "*10}{espaco}
{" "*10}{linha}
""")
