from database.conexao import usar_conexao


def criar_tabela_players(conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
CREATE TABLE IF NOT EXISTS players(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nivel INTEGER NOT NULL,
    exp_necessario INTEGER NOT NULL,
    exp INTEGER NOT NULL,
    mana_maxima INTEGER NOT NULL,
    mana INTEGER NOT NULL,
    vida_maxima INTEGER NOT NULL,
    vida INTEGER NOT NULL,
    defesa INTEGER NOT NULL
)
""")


def get_all(conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("SELECT * FROM players").fetchall()


def get(id, conn=None):
    with usar_conexao(conn) as conn:
        return conn.execute("SELECT * FROM players WHERE id = ?", (id,)).fetchone()


def create(nome, nivel, exp_n, exp, mana_m, mana, vida_m, vida, defesa, conn=None):
    with usar_conexao(conn) as conn:
        cursor = conn.execute("""
            INSERT INTO players (
                nome,
                nivel,
                exp_necessario,
                exp,
                mana_maxima,
                mana,
                vida_maxima,
                vida,
                defesa                    
            )
            VALUES (?,?,?,?,?,?,?,?,?)
        """, (nome, nivel, exp_n, exp, mana_m, mana, vida_m, vida, defesa))
        return cursor.lastrowid


def update(id, nome, nivel, exp_n, exp, mana_m, mana, vida_m, vida, defesa, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("""
            UPDATE players
            SET nome = ?, nivel = ?, exp_necessario = ?,          
            exp, mana_maxima = ?, mana = ?, vida_maxima = ?, vida = ?, defesa = ?
            WHERE id = ?
        """, (nome, nivel, exp_n, exp, mana_m, mana, vida_m, vida, defesa, id))


def delete(id, conn=None):
    with usar_conexao(conn) as conn:
        conn.execute("DELETE FROM players WHERE id = ?", (id,))
