from database.conexao import conectar
from contextlib import closing

def criar_tabela_estados():
    with closing(conectar()) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS estados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
            )
        """)

def get_estados():
    with closing(conectar()) as conn:
        return conn.execute("SELECT * FROM estados").fetchall()

def post_estado(nome):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("INSERT INTO estados (nome) VALUES (?)", (nome,))

def get_estado(id):
    with closing(conectar()) as conn:
        return conn.execute("SELECT * FROM estados WHERE id = ?",(id,)).fetchone()

def update_estado(id, nome):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("UPDATE estados SET nome = ? WHERE id = ?", (nome, id))

def delete_estado(id):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("DELETE FROM estados WHERE id = ?",(id,))