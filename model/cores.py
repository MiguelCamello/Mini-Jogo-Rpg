from interface.formatação import espacamento
from utils.carregar_json import carregar_json
from utils.erros import CorInexistenteError

class Cores:
    def __init__(self):
        self.atualizar()

    def atualizar(self):
        dados = carregar_json(cores=True)["cores"]

        self.PRETO = f"\033[{dados['cores']['preto']}m"
        self.VERMELHO = f"\033[{dados['cores']['vermelho']}m"
        self.DOURADO = f"\033[{dados['cores']['dourado']}m"
        self.AZUL = f"\033[{dados['cores']['azul']}m"
        self.VERDE = f"\033[{dados['cores']['verde']}m"
        self.ROXO = f"\033[{dados['cores']['roxo']}m"
        self.RESET = f"\033[{dados['reset']}m"
        self.FUNDO_CINZA = f"\033[{dados['fundos']['cinza']}m"
        self.FUNDO_PRETO = f"\033[{dados['fundos']['preto']}m"

    def get_codigo(self, cor_req):
        cor_req = cor_req.lower()
        self.atualizar()
        dados = carregar_json(cores=True)["cores"]['cores']

        for cor, codigo in dados.items():
            if cor == cor_req:
                return codigo
        raise CorInexistenteError

    def getAll_codigos(self):
        self.atualizar()
        dados = carregar_json(cores=True)["cores"]['cores']

        cores_dict = {}
        for cor, codigo in dados.items():
            cores_dict[cor] = codigo
        return cores_dict

    def teste_de_cores(self):
        self.atualizar()
        dados = carregar_json(cores=True)["cores"]

        print()
        espacamento(30)
        print(f"{"== Estilos ==":^21}")
        for codigo in dados['estilos_backup'].values():
            espacamento(30)
            print(f"\033[{codigo}m■ {codigo:<3} - |== Teste ==|{self.RESET}")

        print()
        espacamento(30)
        print(f"{"== Texto ==":^21}")
        for codigo in dados['cores_backup'].values():
            espacamento(30)
            print(f"\033[{codigo}m■ {codigo:<3} - |== Teste ==|{self.RESET}")

        print()
        espacamento(30)
        print(f"{"== Fundos ==":^21}")
        for codigo in dados['fundos_backup'].values():
            espacamento(30)
            print(f"\033[{codigo}m■ {codigo:<3} - |== Teste ==|{self.RESET}")


cores_obj = Cores()
