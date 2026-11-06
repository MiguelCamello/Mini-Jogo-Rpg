from wcwidth import wcswidth
import unicodedata
import subprocess
import platform
import time
import re

def limpar_terminal():
    comando = "cls" if platform.system() == "Windows" else "clear"
    subprocess.run(comando, shell=True)

def centralizar(texto, largura):
    texto_limpo = re.sub(r'\033\[[0-9;]*m', '', texto)
    espacos = largura - wcswidth(texto_limpo)

    esquerda = espacos // 2
    direita = espacos - esquerda

    return " " * esquerda + texto + " " * direita

def alinhar_para(texto, largura, direcao):
    texto_limpo = re.sub(r'\033\[[0-9;]*m', '', texto)
    espacos = largura - wcswidth(texto_limpo)

    if direcao == "esquerda":
        return texto + " "*espacos
    
    elif direcao == "direita":
        return " "*espacos + texto

def espacamento(espaco):
    print(" "*espaco, end="")

def slow_print(texto, delay=0.05, cor="\033[0m", end="\n"):
    print(cor, end="")

    for i, letra in enumerate(texto):
        print(letra, end="", flush=True)

        if i < len(texto) - 1:
            time.sleep(delay)

    print("\033[0m", end=end)

def normalizar_texto(texto):
    texto = texto.lower().strip()

    # Remove acentos
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    # Substitui espaços e caracteres especiais por _
    texto = re.sub(r"[^a-z0-9]+", "_", texto)

    # Remove _ do início e do final
    return texto.strip("_")

def descricao_efeito(hab_dados):
    tipos = hab_dados["tipos"]

    if len(tipos) > 1:
        return "/".join(tipo.capitalize() for tipo in tipos)

    tipo = tipos[0]

    if tipo == "dano":
        return f"Dano: {hab_dados['potencia']}"

    elif tipo == "cura":
        return f"Cura: {hab_dados['cura']}"

    elif tipo == "efeito":
        return "Efeito especial"

    return "Sem efeito"