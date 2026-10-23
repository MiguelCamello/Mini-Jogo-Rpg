from database.conexao import conectar

def criar_tabela_players_habilidades():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS players_habilidades(
    player_id INTEGER NOT NULL,
    habilidade_id INTEGER NOT NULL,
     
    PRIMARY KEY (player_id, habilidade_id), 
     
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (habilidade_id) REFERENCES habilidades(id)     
)
""")