from utils.erros import *
import random as rm

class Player:
    def __init__(self,
                hab_json,         
                nome,
                status=["Vivo"],
                nivel=1,
                exp_necessario=200,
                exp=0,
                mana_maxima=50,
                mana=50,
                vida_maxima=100,
                vida=100,
                defesa=10,
                itens=[]
                ):
        self.nome = nome
        self.status = status
        self.nivel = nivel
        self.exp_necessario = exp_necessario
        self.exp = exp
        self.mana_maxima = mana_maxima
        self.mana = mana
        self.vida_maxima = vida_maxima
        self.vida = vida
        self.defesa = defesa
        self.inventario = itens

        habilidades_possiveis = [hab for hab in hab_json.values() if hab["raridade"] == "comum"]
        self.habilidades = rm.sample(habilidades_possiveis, 3)
        
    def morrer(self):
        self.status = ["morto"]
        #vou fazer penalidade

    def tomou_dano(
    self,
    dano,
    penetracao_defesa=0,
    ignorar_defesa=False
    ):
        if ignorar_defesa:
            defesa_aplicada = 0
        else:
            defesa_aplicada = self.defesa * (
                1 - penetracao_defesa / 100
            )
    
        dano_final = max(0, dano - defesa_aplicada)
        self.vida = max(0, self.vida - dano_final)
        if self.vida == 0:
            self.morto()

    def tomou_efeito(self, efeitos):
        for efeito in efeitos:
            if efeito in self.status:
                print(f"O {self.nome} já possui o efeito {efeito}!")
                continue
            self.status.append(efeito)
        

    def ganho_exp(self, exp):
        if exp <= 0: 
            return print("Esse valor é invalido!")
        self.exp += exp

        while self.exp >= self.exp_necessario:
            self.nivel += 1
            self.exp -= self.exp_necessario
        self.calculo_lvlUp()

    def calculo_lvlUp(self):
        self.exp_necessario = 200+(self.nivel**2)
        self.mana_maxima = 100+(self.nivel*2)
        self.vida_maxima = 50+(self.nivel*2)
        self.defesa = round(10+(self.nivel*1.5))

    def ganhar_item(self, item):
        self.inventario.append(item)

    def habilidades_disponiveis(self, habilidades_json):
        return [hab for hab in self.habilidades if habilidades_json[hab]["custo_mana" <= self.mana]]

    def aplicar_habilidade(self, habilidades_json, alvo, habilidade_req):
        habilidade = habilidades_json[habilidade_req]

        if habilidade["tipo"] == "dano":
            alvo.tomou_dano(
                dano=habilidade["potencia"],
                penetracao_defesa=habilidade.get("penetracao_defesa", 0),
                ignorar_defesa=habilidade.get("ignorar_defesa", False)
            )
        if habilidade["tipo"] == "cura":
            self.vida = min(self.vida_maxima, self.vida + habilidade["cura"])

        if habilidade["tipo"] == "efeito":
            self.tomou_efeito(habilidade["efeitos"])

    def usar_habilidade(self, habilidades_json, alvo, habilidade_req):
        if habilidade_req not in habilidades_json:
            raise HabilidadeInexistenteError(f"A habilidade {habilidade_req} não existe no jogo!")

        if habilidade_req not in self.habilidades:
            raise HabilidadeNaoAdquiridaError(f"Você não possui a habilidade {habilidade_req}!")

        if not (hab_disp := self.habilidades_disponiveis(habilidades_json)): # comparador morsa := cria variavel e usa na comparação em 1 linha
            raise ManaInsuficienteError("Você não possui mana suficiente para nenhuma habilidade!")

        if habilidade_req not in hab_disp:
            raise ManaInsuficienteError("Você não possui mana suficiente para está habilidade!")

        self.aplicar_habilidade(habilidades_json, alvo, habilidade_req)
        print(f"{self.nome} usou a habilidade {habilidade_req}")

    def info(self, habilidades_json):
        linha = "+" + "-" * 46 + "+"

        habilidades = "\n".join(
            f"| - {habilidades_json[hab]['nome']:<30} "
            f"Mana: {habilidades_json[hab]['custo_mana']:>5} |"
            for hab in self.habilidades
        )

        itens = "\n".join(
            f"| - {str(itens):<30}|"
            for item in self.itens.items()
        )

        print(f"""
{linha}
|{"FICHA DO PLAYER":^46}|
{linha}
| Nome: {self.nome:<39}|
| Status: {', '.join(self.status):<37}|
{linha}
|{"ATRIBUTOS":<46}|
| Vida: {self.vida:<39}|
| Mana: {self.mana:<39}|
| Defesa: {self.defesa:<37}|
| Experiência: {self.exp:<32}|
{linha}
|{"HABILIDADES":<46}|
{habilidades}
{linha}
|{"INVENTÁRIO":<46}|
{itens}
{linha}
""")