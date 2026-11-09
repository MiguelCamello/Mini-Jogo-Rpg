from sistema.escolher_habilidade import escolher_habilidade
from sistema.menu_principal import menu_principal
from interface.telas.combate import tela_combate

from interface.formatação import limpar_terminal, slow_print, color_print, normalizar_texto, espacamento
from model.cores import cores_obj as c_obj

from utils.criar_classe import criar_player, criar_inimigo

from database.criar_todas_tabelas import criar_todas_tabelas
from database.salvar import salvar_player, obter_players

from utils.carregar_json import carregar_json
from utils.resposta import verificar_resposta
from utils.erros import *

import time

criar_todas_tabelas()

while True:
    opcao = menu_principal()
    if opcao == "novo_jogo":
        limpar_terminal()

        while True:
            espacamento(30)
            slow_print("Qual será o nome do seu personagem?")

            espacamento(30)
            nome_jogador = input(" > ").capitalize().strip()

            espacamento(30)
            slow_print(f"{nome_jogador} é o nome desejado?")

            espacamento(30)
            if verificar_resposta(input(" > ")):
                break

        player_obj = criar_player(nome=nome_jogador)

    if opcao == "carregar_jogo":
        limpar_terminal()
        
        saves = obter_players()

        espacamento(30)
        print(", ".join(f"{save['nome']}" for save in saves))

        espacamento(30)
        slow_print("Qual save deseja carregar?")

        espacamento(30)
        input(" > ")
    break

jogando = True
while jogando:  # loop principal

    while True:  # carregar inimigo
        try:
            limpar_terminal()

            espacamento(30)
            slow_print("Deseja lutar com qual inimigo?")

            espacamento(30)
            inimigo_nome = normalizar_texto(input(" > "))

            if inimigo_nome not in carregar_json(inimigo=True)["inimigos"]:
                raise InimigoInexistenteError

            inimigo_obj = criar_inimigo(nome=inimigo_nome)
            break

        except InimigoInexistenteError:
            color_print("Esse não é um inimigo Válido!")
            time.sleep(2)

    while inimigo_obj.vivo and player_obj.vivo:  # loop combate
        limpar_terminal()

        tela_combate(player_obj=player_obj, inimigo_obj=inimigo_obj)

        slow_print("Qual ação deseja executar?")
        acao = normalizar_texto(input(" > "))

        if acao == "x":
            print("Deseja sair sem salvar?")

        elif acao in ["habilidade", "habilidades"]:  # pra erro ortografico humano

            habilidade = escolher_habilidade(player_obj)

            if habilidade:
                player_obj.usar_habilidade(
                    habilidade_req=habilidade,
                    alvo=inimigo_obj
                )

        elif acao in ["item", "items", "iten", "itens"]:  # pra erro ortografico humano
            print("futuras atualizações")
            time.sleep(1)

        elif acao in ["descansar", "descansa"]:
            player_obj.descansar()
            slow_print(
                f"{player_obj.nome}, descansou e recuperou {c_obj.AZUL}50{c_obj.RESET} de mana!")
            time.sleep(1)

        else:
            color_print("Está não é uma ação valida!")
            time.sleep(2)

        inimigo_obj.atacar(player_obj)
        input("")