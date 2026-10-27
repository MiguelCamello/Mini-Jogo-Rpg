from database.conexao import conectar
from database.tabelas import *
from contextlib import closing

# def criar_todas_tabelas():
#     with closing(conectar()) as conn:
#         with conn:
#             try:
#                 criar_tabela_players(conn=conn)
#                 criar_tabela_players_habilidades(conn=conn)
#                 criar_tabela_players_estados(conn=conn)
#                 criar_tabela_players_itens(conn=conn)
#                 criar_tabela_habilidades(conn=conn)
#                 criar_tabela_estados(conn=conn)
#                 criar_tabela_itens(conn=conn)

#                 print("Todas as tabelas foram criadas com sucesso!")
#             except:
#                 print("Houve um erro na criação das tabelas!")

def criar_todas_tabelas():
    with closing(conectar()) as conn:
        with conn:
            
            criar_tabela_players(conn=conn)
            criar_tabela_habilidades(conn=conn)
            criar_tabela_estados(conn=conn)
            criar_tabela_itens(conn=conn)
            criar_tabela_players_habilidades(conn=conn)
            criar_tabela_players_estados(conn=conn)
            criar_tabela_players_itens(conn=conn)