from database.conexao import conectar
from contextlib import closing

def criar_tabela_players_itens():
    with closing(conectar()) as conn:
        conn.execute("""
CREATE TABLE IF NOT EXISTS players_itens(
    player_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL DEFAULT 1,
                       
    PRIMARY KEY (player_id, item_id),
    
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (item_id) REFERENCES itens(id)
    )
""")


def get_players_itens():
    with closing(conectar()) as conn:
        return conn.execute("SELECT * FROM players_itens").fetchall()

def post_player_item(player_id, item_id, quantidade):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("""
                INSERT INTO players_itens (player_id, item_id) 
                VALUES (?,?)
            """,(player_id, item_id))

def get_player_item(player_id, item_id):
    with closing(conectar()) as conn:
        return conn.execute("""
            SELECT * FROM players_itens 
            WHERE player_id = ? 
            AND item_id = ?
        """,(player_id, item_id)).fetchone()

def update_player_item(player_id, item_id, nova_quantidade):
    with closing(conectar()) as conn:
        with conn:
            if nova_quantidade <= 0:
                delete_player_item(player_id, item_id)
                return
            else:
                conn.execute("""
                    UPDATE players_itens
                    SET quantia = ?
                    WHERE player_id = ?
                    AND item_id = ?
                """, (nova_quantidade, player_id, item_id))

def delete_player_item(player_id, item_id):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("""
                DELETE FROM players_itens 
                WHERE player_id = ? 
                AND item_id = ?
            """,(player_id, item_id))