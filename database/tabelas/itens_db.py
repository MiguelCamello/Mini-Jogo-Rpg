from database.conexao import conectar
from contextlib import closing

def criar_tabela_itens():
    with closing(conectar()) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS itens(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
            )
        """)

def get_itens():
    with closing(conectar()) as conn:
        return conn.execute("SELECT * FROM itens").fetchall()

def post_item(nome):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("INSERT INTO itens (nome) VALUES (?)", (nome,))

def get_item(id):
    with closing(conectar()) as conn:
        return conn.execute("SELECT * FROM itens WHERE id = ?",(id,)).fetchone()

def update_item(id, nome):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("UPDATE itens SET nome = ? WHERE id = ?", (nome, id))

def delete_item(id):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("DELETE FROM itens WHERE id = ?",(id,))