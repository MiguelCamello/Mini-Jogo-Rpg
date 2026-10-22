from utils.erros import *
import random as rm


class Player:
    def __init__(self,
                 habilidades_json,
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
                 itens={}
                 ):
        self.habilidades_json = habilidades_json
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

        habilidades_possiveis = [
            hab for hab, dados in habilidades_json.items() if dados["raridade"] == "comum"]
        self.habilidades = rm.sample(habilidades_possiveis, 3)

    def morrer(self, atacante):
        self.status = ["morto"]

        print(f"Você morreu para um {atacante}")
        # vou fazer penalidade

    def tomou_dano(self, habilidade_tomada, atacante):
        dano = habilidade_tomada["potencia"]
        penetracao_defesa = habilidade_tomada.get("penetracao_defesa", 0)
        ignorar_defesa = habilidade_tomada.get("ignorar_defesa", False)

        if ignorar_defesa:
            defesa_aplicada = 0
        else:
            defesa_aplicada = self.defesa * (
                1 - penetracao_defesa / 100
            )

        dano_final = max(0, dano - defesa_aplicada)
        self.vida = round(max(0, self.vida - dano_final))
        if self.vida == 0:
            self.morto(atacante)

    def tomou_efeito(self, efeitos):
        for efeito in efeitos:
            if efeito in self.status:
                print(f"O {self.nome} já possui o efeito {efeito}!")
                continue
            self.status.append(efeito)

    def ganhou_exp(self, exp):
        if exp <= 0:
            return print("Esse valor de exp é invalido!")
        self.exp += exp

        while self.exp >= self.exp_necessario:
            self.exp -= self.exp_necessario
            self.nivel += 1
            self.calculo_lvlUp()

    def calculo_lvlUp(self):
        self.exp_necessario = 200+(self.nivel**2)
        self.mana_maxima = 50+(self.nivel*2)
        self.vida_maxima = 100+(self.nivel*2)
        self.defesa = round(10+(self.nivel*1.5))

    def ganhou_item(self, item):
        if item not in self.inventario:
            self.inventario[item] = 1
            return
        self.inventario[item] += 1

    def ganhou_habilidade(self, habilidade_adquirida):
        if habilidade_adquirida not in self.habilidades_json:
            raise HabilidadeInexistenteError("Está habilidade não existe!")
        if habilidade_adquirida in self.habilidades:
            return print(f"{self.nome} Ganhou uma habilidade repetida!")

        self.habilidades.append(habilidade_adquirida)

    def habilidades_disponiveis(self):
        return [hab for hab in self.habilidades if self.habilidades_json[hab]["custo_mana"] <= self.mana]

    def aplicar_habilidade(self, alvo, habilidade_req):
        habilidade = self.habilidades_json[habilidade_req]

        if "dano" in habilidade["tipos"]:
            alvo.tomou_dano(habilidade, self)

        if "cura" in habilidade["tipos"]:
            self.vida = min(self.vida_maxima, self.vida + habilidade["cura"])

        if "efeitos" in habilidade["tipos"]:
            alvo.tomou_efeito(habilidade["efeitos"])

        self.mana -= habilidade["custo_mana"]

    def usar_habilidade(self, alvo, habilidade_req):
        if habilidade_req not in self.habilidades_json:
            raise HabilidadeInexistenteError(
                f"A habilidade {habilidade_req} não existe no jogo!")

        if habilidade_req not in self.habilidades:
            raise HabilidadeNaoAdquiridaError(
                f"Você não possui a habilidade {habilidade_req}!")

        # comparador morsa := cria variavel e usa na comparação em 1 linha
        if not (hab_disp := self.habilidades_disponiveis()):
            raise ManaInsuficienteError(
                "Você não possui mana suficiente para nenhuma habilidade!")

        if habilidade_req not in hab_disp:
            raise ManaInsuficienteError(
                "Você não possui mana suficiente para está habilidade!")

        print(f"{self.nome} usou a habilidade {habilidade_req}")
        self.aplicar_habilidade(alvo, habilidade_req)

    def info(self):
        linha = "+" + "-" * 46 + "+"

        habilidades = "\n".join(
            f"| - {self.habilidades_json[hab]['nome']:<30} "
            f"Mana: {self.habilidades_json[hab]['custo_mana']:>5} |"
            for hab in self.habilidades
        )

        itens = "\n".join(
            f"| - {str(item):<28}Quantia: {str(quantia):>5} |"
            for item, quantia in self.inventario.items()
        ) if self.inventario else f"| {'Inventário vazio':^44} |"

        print(f"""
{linha}
|{"FICHA DO PLAYER":^46}|
{linha}
| Nome: {self.nome:<39}|
| Nivel: {self.nivel:<38}|
| Status: {', '.join(self.status):<37}|
{linha}
|{"ATRIBUTOS":<46}|
| Vida: {str(self.vida_maxima)+"/"+str(self.vida):<39}|
| Mana: {str(self.mana_maxima)+"/"+str(self.mana):<39}|
| Defesa: {self.defesa:<37}|
| Experiência: {str(self.exp_necessario)+"/"+str(self.exp):<32}|
{linha}
|{"HABILIDADES":<46}|
{habilidades}
{linha}
|{"INVENTÁRIO":<46}|
{itens:<46}
|{"":<46}|
{linha}
""")