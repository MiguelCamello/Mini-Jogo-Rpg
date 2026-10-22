from utils.carregar_json import carregar_json
import textwrap


def inspecionar_habilidade(habilidade_req):
    habilidade_dados = carregar_json(habilidades=True)['habilidades'].get(habilidade_req)
    if habilidade_dados is None:
        print(f"A habilidade {habilidade_req} não existe!")
        return

    linha = "+" + "-" * 46 + "+"

    

    descricao = habilidade_dados['descricao']
    linhas = textwrap.wrap(descricao, width=40)
    
    descricao = "\n".join(
        f"|    {linha:<42}|"
        for linha in linhas
    )

    print(f"""
{linha}
|{habilidade_dados['nome']:^46}|
{linha}
|{"- Tipos:":<16}{", ".join(habilidade_dados['tipos']):<30}|
|{"- Raridade:":<16}{habilidade_dados['raridade']:<30}|
|{"- Potencia:":<16}{habilidade_dados.get('potencia', '0'):<30}|
|{"- Penetração:":<16}{habilidade_dados.get('penetracao_defesa', '0'):<30}|
|{"- Ignora def:":<16}{habilidade_dados.get('ignorar_defesa', 'Não ignora!'):<30}|
|{"- Efeitos:":<16}{", ".join(habilidade_dados.get('efeitos', ['nenhum'])):<30}|
|{"- Custo mana:":<16}{habilidade_dados['custo_mana']:<30}|
|{"- Descrição:":<46}|
{descricao}
{linha}
""")

def inspecionar_efeito(efeito):
    pass

def inspecionar_item(item):
    pass

inspecionar_habilidade("cura_forte")

