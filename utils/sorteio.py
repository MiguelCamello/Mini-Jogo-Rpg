import random as rm

def sortear_quantidade(quantidade_max):
    quantidades = list(range(3, quantidade_max + 1))

    pesos = [0.5 ** (i) for i in range(len(quantidades))] #list comprehension

    return rm.choices(
        quantidades,
        weights=pesos,
        k=1 #retorna 1 sorteio só
    )[0] #retorna o index 0