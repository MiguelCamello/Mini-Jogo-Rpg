from database.conexao import conectar

def criar_tabela_player():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
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


