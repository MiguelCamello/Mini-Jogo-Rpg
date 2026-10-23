from database.conexao import conectar

def criar_tabela_player():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS player(
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

def criar_tabela_player_status():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS player_status (
player_id INTEGER NOT NULL,
status_id INTEGER NOT NULL,

PRIMARY KEY (player_id, status_id),

FOREIGN KEY (player_id) REFERENCES player(id),
FOREIGN KEY (status_id) REFERENCES status(id)
)
""")

def criar_tabela_status():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS status (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
)
""")