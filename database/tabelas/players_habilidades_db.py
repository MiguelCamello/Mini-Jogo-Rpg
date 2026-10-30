from database.conexao import usar_conexao


def criar_tabela_players_habilidades(conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS players_habilidades(
            player_id INTEGER NOT NULL,
            habilidade_id INTEGER NOT NULL,
            
            PRIMARY KEY (player_id, habilidade_id), 
            
            FOREIGN KEY (player_id) REFERENCES players(id)
                ON DELETE CASCADE,
                
            FOREIGN KEY (habilidade_id) REFERENCES habilidades(id)     
            )
        """)


def get_all(conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("SELECT * FROM players_habilidades").fetchall()


def find_by_playerId(player_id, conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("""
            SELECT * FROM players_habilidades 
            WHERE player_id = ? 
        """, (player_id,)).fetchall()


def create(player_id, habilidade_id, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
            INSERT INTO players_habilidades (player_id, habilidade_id) 
            VALUES (?,?)
        """, (player_id, habilidade_id))

# update desnecessario

def delete_by_playerId(player_id, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
            DELETE FROM players_habilidades 
            WHERE player_id = ? 
        """, (player_id,))
