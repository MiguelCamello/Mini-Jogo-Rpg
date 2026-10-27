from contextlib import closing, contextmanager
from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE = BASE_DIR / "database"
BANCO = DATABASE / "game.db"


def conectar():
    conn = sqlite3.connect(BANCO)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

@contextmanager
def usar_conexao(conn=None):
    if conn is not None:
        yield conn
    else:
        with closing(conectar()) as nova_conn:
            with nova_conn:
                yield nova_conn