from utils.sorteio import sortear_quantidade
import random as rm

class Inimigo:
    def __init__(self, inimigo_json):
        self.nome = inimigo_json["nome"]
        self.status = inimigo_json["status"]
        self.mana_maxima = inimigo_json["mana"]
        self.mana = inimigo_json["mana"]
        self.defesa = inimigo_json["defesa"]
        self.vida_maxima = inimigo_json["vida"]
        self.vida = inimigo_json["vida"]
        self.experiencia = inimigo_json["experiencia"]
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

    def morto(self):
        self.status = ["morto"]
        #ainda vai ser adcionado as recompensas

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
        if self.vida == 0 and "morto" not in self.status:
            self.morto()

    def tomou_efeito(self, efeitos):
        for efeito in efeitos:
            if efeito in self.status:
                print(f"O {self.nome} já possui o efeito {efeito}!")
                continue
            self.status.append(efeito)


    def usar_habilidade(self,alvo,habilidades_json):
        habilidades_disponiveis = [
            id_habilidade #identificador da habilidade dentro do json
            for id_habilidade in self.habilidades
            if habilidades_json[id_habilidade]["custo_mana"] <= self.mana
        ]
        if not habilidades_disponiveis:
            print(f"{self.nome} não tem mana para usar nenhuma habilidade!")
            return

        id_habilidade = rm.choice(habilidades_disponiveis)
        habilidade = habilidades_json[id_habilidade]

        print(f"{self.nome} usou a habilidade {habilidade['nome']}!")

        self.mana -= habilidade["custo_mana"]

        if "dano" in habilidade["tipos"]:
            alvo.tomou_dano(
                habilidade["potencia"],
                penetracao_defesa=habilidade.get("penetracao_defesa", 0),
                ignorar_defesa=habilidade.get("ignorar_defesa", False)
                )

        if "cura" in habilidade["tipos"]:
            self.vida = min(
                self.vida_maxima,
                self.vida + habilidade["cura"]
                )

        if "efeito" in habilidade["tipos"]:
            alvo.tomou_efeito(habilidade["efeitos"])

    def info(self, habilidades_json):
            
        linha = "+" + "-" * 46 + "+"

        habilidades = "\n".join(
            f"| - {habilidades_json[id_habilidade]['nome']:<30} "
            f"Mana: {habilidades_json[id_habilidade]['custo_mana']:>5} |"
            for id_habilidade in self.habilidades
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
| Vida: {self.vida:<39}|
| Mana: {self.mana:<39}|
| Defesa: {self.defesa:<37}|
| Experiência: {self.experiencia:<32}|
{linha}
|{"HABILIDADES":<46}|
{habilidades}
{linha}
|{"DROPS":<46}|
{drops}
{linha}
""")


        