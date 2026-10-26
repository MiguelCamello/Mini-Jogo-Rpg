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

def get_players():
    with closing(conectar()) as conn:
        return conn.execute("SELECT * FROM players").fetchall()

def post_player_(nome, nivel, exp_n, exp, mana_m, mana, vida_m, vida, defesa):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("""
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

def get_player(id):
    with closing(conectar()) as conn:
        with conn:
            return conn.execute("SELECT * FROM players WHERE id = ?", (id,)).fetchone()
        
def update_player(id, nome, nivel, exp_n, exp, mana_m, mana, vida_m, vida, defesa):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("""
                UPDATE players
                SET nome = ?, nivel = ?, exp_necessario = ?,          
                exp, mana_maxima = ?, mana = ?, vida_maxima = ?, vida = ?, defesa = ?
                WHERE id = ?
            """, (nome, nivel, exp_n, exp, mana_m, mana, vida_m, vida, defesa, id))

def delete_player(id):
    with closing(conectar()) as conn:
        with conn:
            conn.execute("DELETE FROM players WHERE id = ?", (id,))

