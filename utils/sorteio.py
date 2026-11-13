import random as rm

def sortear_quantidade(quantidade_max):
    quantidades = list(range(3, quantidade_max + 1))

    pesos = [0.5 ** (i) for i in range(len(quantidades))] #list comprehension

    return rm.choices(
        quantidades,
        weights=pesos,
        k=1 #retorna 1 sorteio só
    )[0] #retorna o index 0

def sortear_drops(chance):
    return rm.random() * 100 < chance



PROGRESSAO = {
1: {
    "comum": 100,
    "raro": 10,
    "epico": 1,
    "lendario": 0.1,
    "mitico": 0
},
5: {
    "comum": 100,
    "raro": 30,
    "epico": 10,
    "lendario": 2,
    "mitico": 0.5
},
10: {
    "comum": 100,
    "raro": 50,
    "epico": 25,
    "lendario": 10,
    "mitico": 3
},
20: {
    "comum": 100,
    "raro": 70,
    "epico": 45,
    "lendario": 25,
    "mitico": 12
}}

# chatgpt que fez, não mexe nessa poha
def obter_pesos(nivel):
    marcos = sorted(PROGRESSAO)

    # Encontra os dois marcos que cercam o nível
    for i in range(len(marcos) - 1):
        nivel_inicial = marcos[i]
        nivel_final = marcos[i + 1]

        if nivel_inicial <= nivel <= nivel_final:
            break
    else:
        return PROGRESSAO[marcos[-1]]

    pesos_iniciais = PROGRESSAO[nivel_inicial]
    pesos_finais = PROGRESSAO[nivel_final]

    proporcao = (
        (nivel - nivel_inicial) /
        (nivel_final - nivel_inicial)
    )

    return {
        raridade: pesos_iniciais[raridade] +
        (pesos_finais[raridade] - pesos_iniciais[raridade])
        * proporcao

        for raridade in pesos_iniciais
    }

def sortear_habilidades(player, habilidades_json):
    
    pesos = obter_pesos(player.nivel)

    candidatas = {
        chave: habilidade
        for chave, habilidade in habilidades_json.items()
        if chave not in player.habilidades
    }

    sorteadas = []

    for _ in range(min(3, len(candidatas))):
        chaves = list(candidatas)

        escolhida = rm.choices(
            chaves,
            weights=[
                pesos[candidatas[chave]["raridade"]]
                for chave in chaves
            ],
            k=1
        )[0]

        sorteadas.append(escolhida)
        del candidatas[escolhida]

    return sorteadas