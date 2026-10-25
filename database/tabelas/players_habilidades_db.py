from database.conexao import conectar
from contextlib import closing

def criar_tabela_players_habilidades():
    with closing(conectar()) as conn:
        conn.execute("""
CREATE TABLE IF NOT EXISTS players_habilidades(
    player_id INTEGER NOT NULL,
    habilidade_id INTEGER NOT NULL,
     
    PRIMARY KEY (player_id, habilidade_id), 
     
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (habilidade_id) REFERENCES habilidades(id)     
)
""")

def get_players_habilidades():
    with closing(conectar()) as conn:
        return conn.execute("SELECT * FROM players_habilidades").fetchall()

def post_player_habilidade(player_id, habilidade_id):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("""
                INSERT INTO players_habilidades (player_id, habilidade_id) 
                VALUES (?,?)
            """,(player_id, habilidade_id))

def get_player_habilidade(player_id, habilidade_id):
    with closing(conectar()) as conn:
        return conn.execute("""
            SELECT * FROM players_habilidades 
            WHERE player_id = ? 
            AND habilidade_id = ?
        """,(player_id, habilidade_id)).fetchone()

# update desnecessario

def delete_player_habilidade(player_id, habilidade_id):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("""
                DELETE FROM players_habilidades 
                WHERE player_id = ? 
                AND habilidade_id = ?
            """,(player_id, habilidade_id))