from interface.formatação import limpar_terminal, espacamento, normalizar_texto, slow_print, color_print
from interface.telas.habilidades import tela_habilidades
from interface.telas.inspect_hab import tela_inspect_hab
from model.cores import cores_obj as c_obj

from utils.resposta import verificar_resposta
from utils.carregar_json import carregar_json
from utils.erros import *
import time

def escolher_habilidade(player_obj):
    escolhendo_hab=True
    while escolhendo_hab:  # escolha de habilidade para se usar
        try:
            limpar_terminal()
            tela_habilidades(player_obj)

            espacamento(10)  # pra centralizar
            slow_print("Que habilidade deseja usar?")

            espacamento(10)  # pra centralizar
            habilidade = normalizar_texto(input(" > "))

            if habilidade == "voltar":
                escolhendo_hab = False
                return

            if habilidade not in carregar_json(habilidades=True)["habilidades"]:
                raise HabilidadeInexistenteError

            if habilidade not in player_obj.habilidades:
                raise HabilidadeNaoAdquiridaError

            limpar_terminal()
            tela_inspect_hab(habilidade)

            espacamento(10)
            slow_print("Deseja usar está habilidade?")

            espacamento(10)
            resposta = normalizar_texto(input(" > "))

            escolhendo_hab = not verificar_resposta(resposta)

            if escolhendo_hab:
                espacamento(10)
                color_print("Não atacou!")
                time.sleep(1)
                return

            return habilidade

        except ManaInsuficienteError:
            espacamento(10)
            color_print(
                f"Mana insuficiente para usar a habilidade {habilidade}!", cor=c_obj.DOURADO)
            time.sleep(2)
        except HabilidadeNaoAdquiridaError:
            espacamento(10)
            color_print(
                f"Habilidade {habilidade} não foi adquirida!", cor=c_obj.DOURADO)
            time.sleep(2)
        except HabilidadeInexistenteError:
            espacamento(10)
            color_print(f"{habilidade} não é uma habilidade valida!")
            time.sleep(2)