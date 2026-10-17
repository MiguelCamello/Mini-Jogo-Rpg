import random as rm

class Player:
    def __init__(self,
                hab_json,         
                nome,
                status=None,
                itens=None
                ):
        self.nome = nome
        self.status = status.copy() if status is not None else ["Vivo"]
        self.nivel = 1
        self.exp_necessario = 200
        self.exp = 0
        self.mana_maxima = 50
        self.mana = 50
        self.vida_maxima = 100
        self.vida = 100
        self.defesa = 10
        self.inventario = itens.copy() if itens is not None else []

        habilidades_possiveis = [hab for hab in hab_json if hab["tipo"] == "comum"]
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
        if self.vida == 0 and "morto" not in self.status:
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

    #habilidade

    


