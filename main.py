from utils.criar_inimigos import criar_inimigo
from utils.carregar_json import carregar_json

goblin = criar_inimigo("goblin")
lobo = criar_inimigo("lobo")

habilidades_json = (dados := carregar_json(habilidades=True)["habilidades"])

goblin.info(habilidades_json)
lobo.info(habilidades_json)