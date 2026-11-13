from utils.sorteio import sortear_quantidade, sortear_drops
from utils.erros import SpriteInexistenteError
from interface.formatação import slow_print
import random as rm

class Inimigo:
    def __init__(self, inimigo_json, habilidades_json, sprites_json):
        self.habilidades_json = habilidades_json
        self.sprites_json = sprites_json
        self.sprite = inimigo_json["sprite"]
        self.nome = inimigo_json["nome"]
        self.estados = []
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


    @property
    def vivo(self):
        return self.vida > 0

    def morrer(self, atacante):
        slow_print(f"{self.nome} foi morto por {atacante.nome}!", delay=0.02)

        self.vivo

        atacante.ganhou_exp(self.exp_drop)
        slow_print(f"{atacante.nome} ganhou {self.exp_drop} de exp!", delay=0.02)

        for item, chance in self.drops.items():
            if sortear_drops(chance):
                atacante.ganhou_item(item)
                slow_print(f"{atacante.nome} ganhou {item}!", delay=0.02)

    def descansar(self):
        self.mana = min(
            self.mana_maxima,
            self.mana + 50
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
        if self.vida == 0 and "morto" not in self.estados:
            self.morrer(atacante)

    def tomou_efeito(self, efeito):
        if efeito in self.estados:
            print(f"O {self.nome} já possui o efeito {efeito}!")
            return
        self.estados.append(efeito)

    def habilidades_disponiveis(self):
        return [hab for hab in self.habilidades if self.habilidades_json[hab]["custo_mana"] <= self.mana]

    def atacar(self, alvo): # é aleatoria
        if not (habilidades_disponiveis := self.habilidades_disponiveis()): # := cria var e usa na comparação na msm linha
            self.descansar()

        habilidade_req = rm.choice(habilidades_disponiveis)
        habilidade = self.habilidades_json[habilidade_req]

        print(f"{self.nome} usou a habilidade {habilidade['nome']}!")

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

    def sprite_dict(self):
        if self.sprite not in self.sprites_json:
            raise SpriteInexistenteError
        return self.sprites_json[self.sprite]
        
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
| Estados: {', '.join(self.estados):<36}|
{linha}
|{"ATRIBUTOS":<46}|
| Vida: {str(self.vida)+"/"+str(self.vida_maxima):<39}|
| Mana: {str(self.mana)+"/"+str(self.mana_maxima):<39}|
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


        