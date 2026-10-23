from database.conexao import conectar

def criar_tabela_habilidades():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS habilidades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
)
""")