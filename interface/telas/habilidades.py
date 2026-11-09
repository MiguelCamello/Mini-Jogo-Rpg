from interface.render.player import habilidades_list
from interface.formatação import centralizar
from model.cores import cores_obj as c_obj


def tela_habilidades(player_obj):
    hab_dict = habilidades_list(player_obj)

    linha, espaco = f"|{"="*72}|", f"|{" "*72}|"

    print(f"""
{" "*10}{linha}
{" "*10}| {c_obj.AZUL}{"Mana atual:":>12} {player_obj.mana:<6}{c_obj.RESET}{"== HABILIDADES ==":<18} {c_obj.PRETO}Comum {c_obj.AZUL}Raro {c_obj.ROXO}Épico {c_obj.DOURADO}Lendário {c_obj.VERMELHO}Mítico {c_obj.RESET}|
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
{" "*10}|  |==========|{" "*58}|
{" "*10}|  |  {c_obj.VERMELHO}Voltar{c_obj.RESET}  |{" "*58}|
{" "*10}{linha}
""")
