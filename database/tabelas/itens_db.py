from database.conexao import usar_conexao


def criar_tabela_itens(conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS itens(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
            )
        """)


def get_all(conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("SELECT * FROM itens").fetchall()


def get(id, conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("SELECT * FROM itens WHERE id = ?", (id,)).fetchone()


def find_by_name(nome, conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("SELECT * FROM itens WHERE nome = ?", (nome,)).fetchone()


def create(nome, conn=None):
    with usar_conexao(conn) as conn:
        cursor = conn.execute("INSERT INTO itens (nome) VALUES (?)", (nome,))
        return cursor.lastrowid


def update(id, nome, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("UPDATE itens SET nome = ? WHERE id = ?", (nome, id))


def delete(id, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("DELETE FROM itens WHERE id = ?", (id,))
