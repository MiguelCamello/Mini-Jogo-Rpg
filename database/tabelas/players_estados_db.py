from database.conexao import conectar
from contextlib import closing


def criar_tabela_players_estados():
    with closing(conectar()) as conn:
        conn.execute("""
CREATE TABLE IF NOT EXISTS players_estados (
    player_id INTEGER NOT NULL,
    estados_id INTEGER NOT NULL,

    PRIMARY KEY (player_id, estados_id),

    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (estados_id) REFERENCES estados(id)
)
""")


def get_players_estados():
    with closing(conectar()) as conn:
        return conn.execute("SELECT * FROM players_estados").fetchall()


def post_player_estado(player_id, estado_id):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("""
                INSERT INTO players_estados (player_id, estado_id) 
                VALUES (?,?)
            """, (player_id, estado_id))


def get_player_estado(player_id, estado_id):
    with closing(conectar()) as conn:
        return conn.execute("""
            SELECT * FROM players_estados 
            WHERE player_id = ? 
            AND estado_id = ?
        """, (player_id, estado_id)).fetchone()

# update desnecessario


def delete_player_estado(player_id, estado_id):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("""
                DELETE FROM players_estados 
                WHERE player_id = ? 
                AND estado_id = ?
            """, (player_id, estado_id))
