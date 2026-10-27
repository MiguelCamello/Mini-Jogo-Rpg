from database.conexao import usar_conexao


def criar_tabela_players_estados(conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS players_estados (
            player_id INTEGER NOT NULL,
            estado_id INTEGER NOT NULL,

            PRIMARY KEY (player_id, estado_id),

            FOREIGN KEY (player_id) REFERENCES players(id),
            FOREIGN KEY (estado_id) REFERENCES estados(id)
            )
        """)


def get_players_estados(conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("SELECT * FROM players_estados").fetchall()


def get_player_estado(player_id, estado_id, conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("""
            SELECT * FROM players_estados 
            WHERE player_id = ? 
            AND estado_id = ?
        """, (player_id, estado_id)).fetchone()


def post_player_estado(player_id, estado_id, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
            INSERT INTO players_estados (player_id, estado_id) 
            VALUES (?,?)
        """, (player_id, estado_id))

# update desnecessario


def delete_player_estado(player_id, estado_id, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
            DELETE FROM players_estados 
            WHERE player_id = ? 
            AND estado_id = ?
        """, (player_id, estado_id))
