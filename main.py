from utils.criar_classe import criar_inimigo, criar_player
import os


goblin = criar_inimigo("goblin")
lobo = criar_inimigo("lobo")

player_1 = criar_player("Miguel", defesa= 0)

# lobo.info(habilidades_json)

# goblin.usar_habilidade(player_1)
# goblin.info()


# player_1.ganhar_item("poção de cura")
# player_1.ganhar_item("poção de cura")
# player_1.ganhar_item("poção de dano")

# player_1.ganhar_habilidade("soco_forte")
# player_1.usar_habilidade(habilidade_req="soco_forte", alvo=goblin)

# player_1.info()

#teste de exp
# while True: 
#     os.system("cls")
#     player_1.info()

#     exp = int(input("> "))

#     player_1.ganho_exp(exp)