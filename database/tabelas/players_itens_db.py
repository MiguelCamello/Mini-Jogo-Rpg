from database.conexao import usar_conexao


def criar_tabela_players_itens(conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS players_itens(
            player_id INTEGER NOT NULL,
            item_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL DEFAULT 1,
                            
            PRIMARY KEY (player_id, item_id),
            
            FOREIGN KEY (player_id) REFERENCES players(id)
                ON DELETE CASCADE,

            FOREIGN KEY (item_id) REFERENCES itens(id)
            )
        """)


def get_all(conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("SELECT * FROM players_itens").fetchall()


def find_by_playerId(player_id, conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("""
            SELECT * FROM players_itens 
            WHERE player_id = ? 
        """, (player_id,)).fetchall()


def create(player_id, item_id, quantidade, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
            INSERT INTO players_itens (player_id, item_id, quantidade) 
            VALUES (?,?,?)
        """, (player_id, item_id, quantidade))


def update(player_id, item_id, nova_quantidade, conn=None):
    with usar_conexao(conn) as conn:
        if nova_quantidade <= 0:
            delete(player_id, item_id)
            return
        else:
            conn.execute("""
                UPDATE players_itens
                SET quantia = ?
                WHERE player_id = ?
                AND item_id = ?
            """, (nova_quantidade, player_id, item_id))


def delete(player_id, item_id, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
            DELETE FROM players_itens 
            WHERE player_id = ? 
            AND item_id = ?
        """, (player_id, item_id))

def delete_by_playerId(player_id, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
            DELETE FROM players_itens 
            WHERE player_id = ? 
        """, (player_id,))