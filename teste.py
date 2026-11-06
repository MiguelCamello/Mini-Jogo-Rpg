from interface.telas.tela_habilidades import tela_habilidades
from interface.telas.tela_inspect_hab import tela_inspect_hab
from interface.telas.tela_combate import tela_combate

from interface.funcoes import limpar_terminal, slow_print, espacamento, normalizar_texto

from sistemas.criar_classe import criar_player, criar_inimigo

from database.criar_todas_tabelas import criar_todas_tabelas
from database.saves import salvar_player

from utils.carregar_json import carregar_json
from utils.erros import *

import time


obj_player_1 = criar_player("Miguel Camellot", estados=["Fortalecido", "Envenenado"], mana=10, habilidades=["soco_fraco","soco_pesado", "golpe_vampirico", "julgamento_divino", "golpe_absoluto", "ira_do_dragao_primordial", "devorador_de_mundos"])

jogando =True
while True:
    slow_print("")
    break
while jogando:
    try:
        slow_print("Deseja lutar com qual inimigo?")
        inimigo_nome = normalizar_texto(input(" > "))
        if inimigo_nome not in carregar_json(inimigo=True)["inimigos"]:
            raise InimigoInexistenteError
        obj_inimigo_1 = criar_inimigo(nome=inimigo_nome)
    except InimigoInexistenteError:
        print("Esse não é um inimigo Válido!")
        time.sleep(2)

    while obj_inimigo_1.vivo and obj_player_1.vivo:
        limpar_terminal()
        tela_combate(player_obj=obj_player_1, inimigo_obj=obj_inimigo_1)
        slow_print("Qual ação deseja executar?")
        acao = normalizar_texto(input(" > "))

        if acao in ["habilidade", "habilidades"]: # pra erro ortografico humano
            escolhendo_hab = True
            while escolhendo_hab:
                try:
                    limpar_terminal()
                    tela_habilidades(obj_player_1)

                    espacamento(10) # pra centralizar
                    slow_print("Que habilidade deseja usar?")

                    espacamento(10) # pra centralizar
                    habilidade = normalizar_texto(input(" > "))
                    if habilidade == "voltar": break
                    if habilidade not in carregar_json(habilidades=True)["habilidades"]:
                        raise HabilidadeInexistenteError
                    if habilidade not in obj_player_1.habilidades:
                        raise HabilidadeNaoAdquiridaError

                    limpar_terminal()
                    tela_inspect_hab(habilidade)

                    espacamento(10)
                    slow_print("Deseja usar está habilidade?")

                    espacamento(10)
                    resposta = normalizar_texto(input(" > "))
                    if resposta == "sim": escolhendo_hab=False
                    obj_player_1.usar_habilidade(alvo=obj_inimigo_1, habilidade_req=habilidade)
                except ManaInsuficienteError:
                    espacamento(10)
                    print(f"Você não tem mana suficiente para usar a habilidade {habilidade}!")  
                    time.sleep(2)          
                except HabilidadeNaoAdquiridaError:
                    espacamento(10)
                    print(f"A habilidade {habilidade} não foi adquirida!")
                    time.sleep(2)
                except HabilidadeInexistenteError:
                    espacamento(10)
                    print(f"{habilidade} não é uma habilidade valida!")
                    time.sleep(2)

        elif acao in ["item", "items", "iten", "itens"]: # pra erro ortografico humano
            print("nn fiz ainda")
            time.sleep(1)

        elif acao in ["descansar", "descansa"]:
            obj_player_1.descansar()

        else:
            print("Essa não é uma ação valida!")
            time.sleep(1)
