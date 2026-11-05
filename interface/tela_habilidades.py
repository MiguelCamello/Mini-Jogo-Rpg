from interface.funcoes import centralizar
from interface.render import (habilidades)
from interface.cores import RESET, PRETO, AZUL, ROXO, DOURADO

def tela_habilidades(player_obj):
    hab_dict = habilidades(player_obj)
    linha, espaco = f"|{"="*72}|", f"|{" "*72}|"
    print(f"""
{" "*10}{linha}
{" "*10}|{"Mana atual:":>15} {AZUL}{player_obj.mana:<8}{RESET} {"== HABILIDADES ==":<20} {PRETO}Comum {AZUL}Raro {ROXO}Épico {DOURADO}Lendário {RESET}|
{" "*10}{linha}
{" "*10}{espaco}
{" "*10}|{" "*5}{'== Nome ==':<30}{'== Efeito ==':<15}{'== Custo Mana ==':<22}|
{" "*10}{espaco}
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l1", ""),70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l2", ""),70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l3", ""),70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l4", ""),70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l5", ""),70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l6", ""),70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l7", ""),70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l8", ""),70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l9", ""),70)} |
{" "*10}{espaco}
{" "*10}| {centralizar(hab_dict.get("l10", ""),70)} |
{" "*10}{espaco}
{" "*10}{espaco}
{" "*10}{espaco}
{" "*10}{linha}
""")