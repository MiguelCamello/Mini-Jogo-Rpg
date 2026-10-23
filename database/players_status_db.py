from database.conexao import conectar

def criar_tabela_player_status():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS players_status (
    player_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,

    PRIMARY KEY (player_id, status_id),

    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (status_id) REFERENCES status(id)
)
""")