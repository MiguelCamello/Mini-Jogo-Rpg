from database.conexao import conectar
from contextlib import closing

def criar_tabela_habilidades():
    with closing(conectar()) as conn:
        conn.execute("""
CREATE TABLE IF NOT EXISTS habilidades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
)
""")

def get_habilidades():
    with closing(conectar()) as conn:
        return conn.execute("SELECT * FROM habilidades").fetchall()

def post_habilidade(nome):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("INSERT INTO habilidades (nome) VALUES (?)", (nome,))

def get_habilidade(id):
    with closing(conectar()) as conn:
        return conn.execute("SELECT * FROM habilidades WHERE id = ?",(id,)).fetchone()

def update_habilidade(id, nome):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("UPDATE habilidades SET nome = ? WHERE id = ?", (nome, id))

def delete_habilidade(id):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("DELETE FROM habilidades WHERE id = ?",(id,))