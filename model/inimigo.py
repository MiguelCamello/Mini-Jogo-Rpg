from utils.sorteio import sortear_quantidade, sortear_drops
from utils.erros import ManaInsuficienteError
import random as rm

class Inimigo:
    def __init__(self, inimigo_json, habilidades_json):
        self.habilidades_json = habilidades_json
        self.nome = inimigo_json["nome"]
        self.status = inimigo_json["status"]
        self.mana_maxima = inimigo_json["mana"]
        self.mana = inimigo_json["mana"]
        self.vida_maxima = inimigo_json["vida"]
        self.vida = inimigo_json["vida"]
        self.defesa = inimigo_json["defesa"]
        self.exp_drop = inimigo_json["exp_drop"]
        self.drops = inimigo_json["drops"]

        habilidades_possiveis = inimigo_json["habilidades_possiveis"]

        if len(habilidades_possiveis) <= 3:
            quantidade = len(habilidades_possiveis)
        else:
            quantidade = sortear_quantidade(len(habilidades_possiveis))

        self.habilidades = rm.sample(habilidades_possiveis, quantidade)

    def descansar(self):
        self.mana = min(
            self.mana_maxima,
            self.mana + 20
        )

    def morto(self, atacante):
        print(f"{self.nome} foi morto por {atacante.nome}!")

        self.status = ["morto"]
        atacante.ganhou_exp(self.exp_drop)
        print(f"{atacante.nome} ganhou {self.exp_drop} de exp!")

        for item, chance in self.drops.items():
            if sortear_drops(chance):
                atacante.ganhou_item(item)
                print(f"{atacante.nome} ganhou {item}!")


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
        if self.vida == 0 and "morto" not in self.status:
            self.morto(atacante)

    def tomou_efeito(self, efeitos):
        for efeito in efeitos:
            if efeito in self.status:
                print(f"O {self.nome} já possui o efeito {efeito}!")
                continue
            self.status.append(efeito)

    def habilidades_disponiveis(self):
        return [hab for hab in self.habilidades if self.habilidades_json[hab]["custo_mana"] <= self.mana]

    def usar_habilidade(self, alvo): # é aleatoria
        if not (habilidades_disponiveis := self.habilidades_disponiveis()): # := cria var e usa na comparação na msm linha
            raise ManaInsuficienteError(f"{self.nome} não tem mana para usar nenhuma habilidade!")

        habilidade_req = rm.choice(habilidades_disponiveis)
        habilidade = self.habilidades_json[habilidade_req]

        print(f"{self.nome} usou a habilidade {habilidade['nome']} no {alvo.nome}!")

        self.mana -= habilidade["custo_mana"]

        if "dano" in habilidade["tipos"]:
            alvo.tomou_dano(habilidade, self)

        if "cura" in habilidade["tipos"]:
            self.vida = min(self.vida_maxima, self.vida + habilidade["cura"])

        if "efeito" in habilidade["tipos"]:
            alvo.tomou_efeito(habilidade["efeitos"])

    def info(self):
            
        linha = "+" + "-" * 46 + "+"

        habilidades = "\n".join(
            f"| - {self.habilidades_json[hab]['nome']:<30} "
            f"Mana: {self.habilidades_json[hab]['custo_mana']:>5} |"
            for hab in self.habilidades
        )

        drops = "\n".join(
            f"| - {str(drop):<30} Chance: {valor}% |"
            for drop, valor in self.drops.items()
        )

        print(f"""
{linha}
|{"FICHA DO INIMIGO":^46}|
{linha}
| Nome: {self.nome:<39}|
| Status: {', '.join(self.status):<37}|
{linha}
|{"ATRIBUTOS":<46}|
| Vida: {str(self.vida_maxima)+"/"+str(self.vida):<39}|
| Mana: {str(self.mana_maxima)+"/"+str(self.mana):<39}|
| Defesa: {self.defesa:<37}|
| Experiência: {self.exp_drop:<32}|
{linha}
|{"HABILIDADES":<46}|
{habilidades}
{linha}
|{"DROPS":<46}|
{drops}
{linha}
""")


        