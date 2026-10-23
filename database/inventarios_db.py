from database.conexao import conectar

def criar_tabela_inventario():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS inventarios(
    player_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
                       
    PRIMARY KEY (player_id, item_id),
    
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (item_id) REFERENCES itens(id)
    )
""")