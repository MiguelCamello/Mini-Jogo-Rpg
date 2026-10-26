from tabelas.players_db import criar_tabela_player
from tabelas.players_habilidades_db import criar_tabela_players_habilidades
from tabelas.players_estados_db import criar_tabela_players_status
from tabelas.players_itens_db import criar_tabela_players_itens
from tabelas.habilidades_db import criar_tabela_habilidades
from tabelas.estados_db import criar_tabela_status
from tabelas.itens_db import criar_tabela_itens

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