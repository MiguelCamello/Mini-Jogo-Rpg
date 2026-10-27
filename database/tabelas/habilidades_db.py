from database.conexao import usar_conexao

def criar_tabela_habilidades(conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS habilidades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
            )
        """)

def get_habilidades(conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("SELECT * FROM habilidades").fetchall()


def get_habilidade(id, conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("SELECT * FROM habilidades WHERE id = ?", (id,)).fetchone()


def get_habilidade_peloNome(nome, conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("SELECT * FROM habilidades WHERE nome = ?", (nome,)).fetchone()


def post_habilidade(nome, conn=None):
    with usar_conexao(conn) as conn:
        cursor = conn.execute("INSERT INTO habilidades (nome) VALUES (?)", (nome,))
        return cursor.lastrowid

def update_habilidade(id, nome, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute(
                "UPDATE habilidades SET nome = ? WHERE id = ?", (nome, id))


def delete_habilidade(id, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("DELETE FROM habilidades WHERE id = ?", (id,))
