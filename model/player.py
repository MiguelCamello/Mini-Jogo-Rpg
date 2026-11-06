from utils.erros import *
import random as rm

class Player:
    def __init__(self,
                 habilidades_json,
                 nome,
                 estados=[],
                 nivel=1,
                 exp_necessario=200,
                 exp=0,
                 mana_maxima=50,
                 mana=50,
                 vida_maxima=100,
                 vida=100,
                 defesa=10,
                 itens={},
                 habilidades=None
                 ):
        self.habilidades_json = habilidades_json
        self.nome = nome
        self.estados = estados
        self.nivel = nivel
        self.exp_necessario = exp_necessario
        self.exp = exp
        self.mana_maxima = mana_maxima
        self.mana = mana
        self.vida_maxima = vida_maxima
        self.vida = vida
        self.defesa = defesa
        self.inventario = itens

        if habilidades is None:
            habilidades_possiveis = [
                hab for hab, dados in habilidades_json.items() if dados["raridade"] == "comum"]
            self.habilidades = rm.sample(habilidades_possiveis, 3)
        else:
            self.habilidades = [hab.lower() for hab in habilidades]

    @property
    def vivo(self):
        return self.vida > 0

    def morrer(self, atacante):
        self.vivo
        print(f"Você morreu para um {atacante}")
        # vou fazer penalidade

    def descansar(self):
        self.mana = min(
            self.mana_maxima,
            self.mana + 20
        )

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
            self.morrer(atacante)

    def tomou_efeito(self, efeito):
        if efeito in self.estados:
            print(f"O {self.nome} já possui o efeito {efeito}!")
            return
        self.estados.append(efeito)

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
        #restaura vida, mana
        self.vida = self.vida_maxima
        self.mana = self.mana_maxima

    def ganhou_item(self, item, quantia=1):
        if item not in self.inventario:
            self.inventario[item] = quantia
            return
        self.inventario[item] += quantia

    def ganhou_habilidade(self, habilidade_adquirida):
        habilidade_adquirida = habilidade_adquirida.lower()

        if habilidade_adquirida not in self.habilidades_json:
            raise HabilidadeInexistenteError("Está habilidade não existe!")
        if habilidade_adquirida in self.habilidades:
            return print(f"{self.nome} Ganhou uma habilidade repetida!")
        
        self.habilidades.append(habilidade_adquirida)

    def deletar_habilidade(self, habilidade_del):
        habilidade_del = habilidade_del.lower()

        if habilidade_del not in self.habilidades:
            raise HabilidadeNaoAdquiridaError
        
        self.habilidades.remove(habilidade_del)

    def habilidades_disponiveis(self):
        return [hab for hab in self.habilidades if self.habilidades_json[hab]["custo_mana"] <= self.mana]

    def aplicar_habilidade(self, alvo, habilidade_req):
        habilidade = self.habilidades_json[habilidade_req]

        if "dano" in habilidade["tipos"]:
            alvo.tomou_dano(habilidade, self)

        if "cura" in habilidade["tipos"]:
            self.vida = min(self.vida_maxima, self.vida + habilidade["cura"])

        if "efeito" in habilidade["tipos"]:
            for efeito in habilidade["efeitos"]:
                if efeito["alvo"] == "proprio":
                    self.tomou_efeito(efeito["nome"])
                elif efeito["alvo"] == "inimigo":
                    alvo.tomou_efeito(efeito["nome"])

        self.mana -= habilidade["custo_mana"]

    def usar_habilidade(self, alvo, habilidade_req):
        habilidade_req = habilidade_req.lower()

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
        linha = "+"+"-"*46+"+"

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
| Estados: {', '.join(self.estados):<36}|
{linha}
|{"ATRIBUTOS":<46}|
| Vida: {str(self.vida)+"/"+str(self.vida_maxima):<39}|
| Mana: {str(self.mana)+"/"+str(self.mana_maxima):<39}|
| Defesa: {self.defesa:<37}|
| Experiência: {str(self.exp)+"/"+str(self.exp_necessario):<32}|
{linha}
|{"HABILIDADES":<46}|
{habilidades}
{linha}
|{"INVENTÁRIO":<46}|
{itens:<46}
|{"":<46}|
{linha}
""")