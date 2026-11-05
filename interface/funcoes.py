from wcwidth import wcswidth
import re
import subprocess
import platform

def limpar_terminal():
    comando = "cls" if platform.system() == "Windows" else "clear"
    subprocess.run(comando, shell=True)

def centralizar(texto, largura):
    texto_limpo = re.sub(r'\033\[[0-9;]*m', '', texto)
    espacos = largura - wcswidth(texto_limpo)

    esquerda = espacos // 2
    direita = espacos - esquerda

    return " " * esquerda + texto + " " * direita

def descricao_efeito(hab_dados):
    tipos = hab_dados["tipos"]
    potencia = hab_dados.get("potencia", 0)

    if "dano" in tipos:
        return f"Dano: {potencia}"

    elif "cura" in tipos:
        return f"Cura: {potencia}"

    elif "efeito" in tipos:
        return "Efeito especial"

    return "Sem efeito"