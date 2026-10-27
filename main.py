from sistemas.criar_classe import criar_inimigo, criar_player
from sistemas.busca import buscar_objeto
from database.saves import salvar_player
import time
import os


goblin = criar_inimigo("goblin")
lobo = criar_inimigo("lobo")

inimigos_list = [goblin, lobo]

player_1 = criar_player("Miguel")

# lobo.info(habilidades_json)

# goblin.usar_habilidade(player_1)
# goblin.info()


# player_1.ganhou_item("poção de cura")
# player_1.ganhou_item("poção de cura")
# player_1.ganhou_item("poção de dano")

# player_1.ganhou_habilidade("soco_forte")
# player_1.usar_habilidade(habilidade_req="soco_forte", alvo=goblin)

# player_1.info()

#teste de exp
# while True: 
#     os.system("cls")
#     player_1.info()

#     exp = int(input("> "))

#     player_1.ganho_exp(exp)

#teste geral
while True: 
    try:
        os.system("cls")
        player_1.info()

        print("exp, item, habilidade, info, salvar")
        print(" oque quer fazer?")
        opcao = input("> ")

        if opcao == "exp":
            print(" quanto de exp vc vai ganhar")
            exp = int(input("> "))
            player_1.ganhou_exp(exp)

        elif opcao == "item":
            print(" que itens deseja ganhar? separe por virgula ,")
            itens = input("> ")
            itensList = [item for item in itens.split(", ")]
            for item in itensList:
                player_1.ganhou_item(item)

        elif opcao == "habilidade":
            print(" Quem deseja atacar?")
            alvo = input("> ")
            print(", ".join(player_1.habilidades))
            print(" Qual habilidade deseja usar?")
            habilidade = input("> ")

            if (alvo_obj := buscar_objeto(alvo, inimigos_list)) is None:
                print(" Esse alvo não existe")
            else:
                player_1.usar_habilidade(alvo_obj, habilidade)
                time.sleep(1)
            if "morto" in alvo_obj.status:
                inimigos_list.remove(alvo_obj)
                input("> ")

        elif opcao == "info":
            print(" Quer informação de quem?")
            alvo = input("> ")
            alvo_obj = buscar_objeto(alvo, inimigos_list)
            os.system("cls")
            alvo_obj.info()
            input("continuar> ")

        elif opcao == "salvar":
            salvar_player(player_1)
    except:
        print()
        time.sleep(1)

