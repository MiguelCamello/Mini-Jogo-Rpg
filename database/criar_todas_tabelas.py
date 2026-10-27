from database.tabelas.players_db import criar_tabela_player
from database.tabelas.players_habilidades_db import criar_tabela_players_habilidades
from database.tabelas.players_estados_db import criar_tabela_players_estados
from database.tabelas.players_itens_db import criar_tabela_players_itens
from database.tabelas.habilidades_db import criar_tabela_habilidades
from database.tabelas.estados_db import criar_tabela_estados
from database.tabelas.itens_db import criar_tabela_itens

def criar_todas_tabelas():
    try:
        criar_tabela_player()
        criar_tabela_players_habilidades()
        criar_tabela_players_estados()
        criar_tabela_players_itens()
        criar_tabela_habilidades()
        criar_tabela_estados()
        criar_tabela_itens()

        print("Todas as tabelas foram criadas com sucesso!")
    except:
        print("Houve um erro na criação das tabelas!")