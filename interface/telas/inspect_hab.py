from interface.render.player import formatar_estados, formatar_raridade
from utils.carregar_json import carregar_json
from interface.formatação import alinhar_para
from model.cores import cores_obj as c_obj
import textwrap

espada = {
"l1": r"     /\    ",
"l2": r"    //\\    ",
"l3": r"   //  \\   ",
"l4": "   ||  ||   ",
"l5": "   ||  ||   ",
"l6": "   ||  ||   ",
"l7": "   ||  ||   ",
"l8": "   ||  ||   ",
"l9": "   ||  ||   ",
"l10": "   ||  ||   ",
"l11": "   ||  ||   ",
"l12": "   ||  ||   ",
"l13": "   ||  ||   ",
"l14": "   ||  ||   ",
"l15": "<====()====>",
"l16": r"    |/\|    ",
"l17": r"    |\/|    ",
"l18": r"    |/\|    ",
"l19": r"    |\/|    ",
"l20": r"    /  \    ",
"l21": r"    \__/    ",
}

def tela_inspect_hab(habilidade_req):
    hab = carregar_json(habilidades=True)["habilidades"][habilidade_req]
    linha, espaco = f"|{"="*72}|", f"|{" "*72}|"

    cor = formatar_raridade(hab)

    tipos = hab["tipos"]

    tipo1 = f"[{tipos[0]}]" if len(tipos) > 0 else "N/A"
    tipo2 = f"[{tipos[1]}]" if len(tipos) > 1 else ""

    potencia = hab.get("potencia", "N/A")
    cura = hab.get("cura", "N/A")
    penetracao = hab.get("penetracao_defesa", "N/A")
    ignorar_defesa = "Sim" if hab.get("ignorar_defesa", False) else "Não"


    efeitos_list = [efeito["nome"] for efeito in hab.get("efeitos", [])]
    alvo_list = [efeito["alvo"] for efeito in hab.get("efeitos", [])]

    if not efeitos_list:
        efeitos = "N/A"
        alvo = "N/A"
    else:
        efeitos = formatar_estados(efeitos_list)
        alvo = " ".join(f"[{alvo}]" for alvo in alvo_list)

    descricao = hab['descricao']
    linhas = textwrap.wrap(descricao, width=20)
    linhas = (linhas + [""] * 4)[:4]

    print(f"""
{" "*10}{linha}
{" "*10}|{cor}{"== "+hab['nome']+" ==":^72}{c_obj.RESET}|
{" "*10}{linha}
{" "*10}{espaco}
{" "*10}{espaco}
{" "*10}{espaco}
{" "*10}|{             '== Tipos ==':>28}{cor}{ espada['l1']:^16}{c_obj.RESET}{'== Custo ==':<28}|
{" "*10}|{" "*28                        }{cor}{ espada['l2']:^16}{c_obj.RESET}{" "*28}|
{" "*10}|{                     tipo1:>28}{cor}{ espada['l3']:^16}{c_obj.RESET}{hab['custo_mana']:<28}|
{" "*10}|{                     tipo2:>28}{cor}{ espada['l4']:^16}{c_obj.RESET}{" "*28}|
{" "*10}|{" "*28                        }{cor}{ espada['l5']:^16}{c_obj.RESET}{" "*28}|
{" "*10}|{              '== Dano ==':>28}{cor}{ espada['l6']:^16}{c_obj.RESET}{'== Cura ==':<28}|
{" "*10}|{" "*28                        }{cor}{ espada['l7']:^16}{c_obj.RESET}{" "*28}|
{" "*10}|{                  potencia:>28}{cor}{ espada['l8']:^16}{c_obj.RESET}{cura:<28}|
{" "*10}|{" "*28                        }{cor}{ espada['l9']:^16}{c_obj.RESET}{" "*28}|
{" "*10}|{" "*28                        }{cor}{ espada['l10']:^16}{c_obj.RESET}{" "*28}|
{" "*10}|{        '== Penetração ==':>28}{cor}{ espada['l11']:^16}{c_obj.RESET}{'== Ignorar Defesa ==':<28}|
{" "*10}|{" "*28                        }{cor}{ espada['l12']:^16}{c_obj.RESET}{" "*28}|
{" "*10}|{                penetracao:>28}{cor}{ espada['l13']:^16}{c_obj.RESET}{ignorar_defesa:<28}|
{" "*10}|{" "*28                        }{cor}{ espada['l14']:^16}{c_obj.RESET}{" "*28}|
{" "*10}|{" "*28            }{c_obj.PRETO}{ espada['l15']:^16}{c_obj.RESET}{" "*28}|
{" "*10}|{                '== Efeitos ==':>28}{ espada['l16']:^16}{c_obj.RESET}{'== Descrição ==':<28}|
{" "*10}|{" "*28                             }{ espada['l17']:^16}{c_obj.RESET}{" "*28}|
{" "*10}|{alinhar_para(efeitos,28, "direita")}{ espada['l18']:^16}{c_obj.RESET}{linhas[0]:<28}|
{" "*10}|{                           alvo:>28}{ espada['l19']:^16}{c_obj.RESET}{linhas[1]:<28}|
{" "*10}|{" "*28                        }{cor}{ espada['l20']:^16}{c_obj.RESET}{linhas[2]:<28}|
{" "*10}|{             '== Alvos ==':>28}{cor}{ espada['l21']:^16}{c_obj.RESET}{linhas[3]:<28}|
{" "*10}{espaco}
{" "*10}{espaco}
{" "*10}{linha}
""")
