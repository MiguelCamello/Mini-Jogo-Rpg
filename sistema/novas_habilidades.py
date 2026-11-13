from interface.formatação import limpar_terminal, slow_print, color_print, normalizar_texto
from model.cores import cores_obj as c_obj

from utils.erros import *


def novas_habilidades(player_obj, hab_sorteadas):
    while True:
        limpar_terminal()
        slow_print(f"Voce pode aprender novas habilidades! \n",cor=c_obj.VERDE)
        try:
            if hab_sorteadas:
                print(", ".join(hab_sorteadas))
                slow_print("Qual destas habilidades deseja aprender?")
                hab = normalizar_texto(input(" > "))
                
                if hab not in hab_sorteadas:
                    raise NameError
                
                player_obj.ganhou_habilidade(hab)
                slow_print(f"{player_obj} Aprendeu a habilidade {hab}!", cor=c_obj.VERDE)
                break
            break

        except HabilidadeInexistenteError:
            color_print("Está habilidade não existe!")
        except NameError:
                    color_print("Está habilidade não é uma opção!")