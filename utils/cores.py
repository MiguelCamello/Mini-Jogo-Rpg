RESET = "\033[0m"
cores = {
    "preto": 30,
    "rosa": 31,
    "verde_claro": 32,
    "verde": 92,
    "laranja": 33,
    "amarelo": 93,
    "roxo": 34,
    "vermelho": 35,
    "vermelho_escuro": 91,
    "azul": 96,
    "azul_escuro": 94,
    "ciano": 36,
    "branco": 37,
    "branco_branco": 97,
}
fundos={
    "preto": 40,
    "cinza": 100,
    "branco": 107,
    "cinza_claro": 47,
    "vermelho": 45,
    "vermelho_claro": 101,
    "rosa": 41,
    "roxo": 44,
    "magenta": 105,
    "azul": 106,
    "azul_escuro": 104,
    "ciano": 46,
    "verde_claro": 42,
    "verde": 102,
    "laranja": 43,
    "amarelo": 103,
}

for nome, codigo in cores.items():
    print(f"\033[{codigo}m■ {codigo} - {nome}\033[0m")

for nome, codigo in fundos.items():
    print(f"\033[{codigo}m■ {codigo} - {nome}\033[0m")