from sistema.escolher_habilidade import escolher_habilidade
from sistema.menu_principal import menu_principal
from sistema.menu_pause import menu_pause
from sistema.menu_saves import menu_saves
from interface.telas.combate import tela_combate

from interface.formatação import limpar_terminal, slow_print, color_print, normalizar_texto
from model.cores import cores_obj as c_obj


from database.criar_todas_tabelas import criar_todas_tabelas

from utils.criar_classe import criar_inimigo
from utils.carregar_json import carregar_json
from utils.erros import *

import time

criar_todas_tabelas()

jogo_rodando=True
while jogo_rodando:
    while True:
        menu_principal()
        
        player_obj = menu_saves()

        break

    jogando = True
    while jogando:  # loop principal

        while True:  # carregar inimigo
            try:
                limpar_terminal()

                slow_print("Deseja lutar com qual inimigo?")

                inimigo_nome = normalizar_texto(input(" > "))

                if inimigo_nome not in carregar_json(inimigo=True)["inimigos"]:
                    raise InimigoInexistenteError

                inimigo_obj = criar_inimigo(nome=inimigo_nome)
                break

            except InimigoInexistenteError:
                color_print("Esse não é um inimigo Válido!")
                time.sleep(2)

        while inimigo_obj.vivo and player_obj.vivo and jogando:  # loop combate
            
            

            escolhendo_acao=True
            while escolhendo_acao:

                limpar_terminal()

                tela_combate(player_obj=player_obj, inimigo_obj=inimigo_obj)

                slow_print("Qual ação deseja executar?")
                acao = normalizar_texto(input(" > "))

                if acao == "pause":

                    sair = menu_pause(player_obj)
                    if sair == "sair":
                        jogando = False
                        break
                    

                elif acao in ["habilidade", "habilidades"]:  # pra erro ortografico humano

                    habilidade = escolher_habilidade(player_obj)
                    time.sleep(0.5)

                    print()

                    if habilidade:
                        player_obj.usar_habilidade(
                            habilidade_req=habilidade,
                            alvo=inimigo_obj
                        )
                    print()
                    escolhendo_acao=False

                elif acao in ["item", "items", "iten", "itens"]:  # pra erro ortografico humano
                    print("futuras atualizações")
                    time.sleep(1)

                elif acao in ["descansar", "descansa"]:
                    player_obj.descansar()
                    slow_print(
                        f"{player_obj.nome}, descansou e recuperou {c_obj.AZUL}50{c_obj.RESET} de mana!")
                    time.sleep(1)
                    escolhendo_acao=False

                elif acao == "exp":
                    exp = int(input())
                    player_obj.ganhou_exp(exp)

                else:
                    color_print("Está não é uma ação valida!")
                    time.sleep(2)

            if inimigo_obj.vivo and player_obj.vivo and jogando:

                inimigo_obj.atacar(player_obj)
                input("")