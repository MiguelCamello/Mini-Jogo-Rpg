from interface.formatação import limpar_terminal, espacamento, normalizar_texto, slow_print, color_print
from interface.telas.menu import tela_pause
from sistema.configuracao import configuracao
from utils.resposta import verificar_resposta
from database.salvar import atualizar_player
from model.cores import cores_obj as c_obj

import time

def menu_pause(player_obj):
    menu_aberto = True
    while menu_aberto:
        limpar_terminal()

        tela_pause()

        espacamento(30)
        slow_print("O'que deseja fazer?")

        espacamento(30)
        acao = normalizar_texto(input(" > "))

        if acao == "continuar":
            return

        if acao in ["configuracao", "configuracoes"]:
            configuracao()

        elif acao in ["salvar", "salva"]:
            limpar_terminal()

            espacamento(30)
            slow_print("O inimigo não sera salvo, apenas o estado atual do player!")

            espacamento(30)
            print("salvando", end="")
            slow_print("...", delay=0.5)

            atualizar_player(player_id=player_obj.id, player_obj=player_obj)

            espacamento(30)
            color_print(f"Dados de {player_obj.nome} foram salvos com sucesso!", cor=c_obj.VERDE)

            time.sleep(2)

        elif acao == "sair":
            limpar_terminal()
            
            espacamento(30)
            slow_print("Deseja salvar antes de sair?")
            espacamento(30)
            slow_print("O inimigo não sera salvo, apenas o estado atual do player!")

            espacamento(30)
            salvar = normalizar_texto(input(" > "))

            if not verificar_resposta(salvar):
                return "sair"

            espacamento(30)
            print("salvando", end="")
            slow_print("...", delay=0.5)

            atualizar_player(player_id=player_obj.id, player_obj=player_obj)

            espacamento(30)
            color_print(f"Dados de {player_obj.nome} foram salvos com sucesso!", cor=c_obj.VERDE)

            time.sleep(2)
