from database.conexao import conectar
from contextlib import closing

def criar_tabela_player():
    with closing(conectar()) as conn:
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


