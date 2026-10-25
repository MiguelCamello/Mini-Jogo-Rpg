from database.tabelas import *

def criar_todas_tabelas():
    try:
        criar_tabela_player()
        criar_tabela_players_habilidades()
        criar_tabela_players_status()
        criar_tabela_players_itens()
        criar_tabela_habilidades()
        criar_tabela_status()
        criar_tabela_itens()

        print("Todas as tabelas foram criadas com sucesso!")
    except:
        print("Houve um erro na criação das tabelas!")