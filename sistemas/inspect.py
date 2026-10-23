from utils.carregar_json import carregar_json
import textwrap


def inspecionar_habilidade(habilidade_req):
    habilidade_dados = carregar_json(habilidades=True)['habilidades'].get(habilidade_req)
    if habilidade_dados is None:
        print(f"A habilidade {habilidade_req} não existe!")
        return

    linha = "+"+"-"*46+"+"

    

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

def inspecionar_efeito(efeito_req):
    efeito_dados = carregar_json(efeitos=True)['efeitos'].get(efeito_req)
    if efeito_dados is None:
        print(f"O efeito {efeito_req} não existe!")
        return 

    linha = "+"+"-"*46+"+"

    descricao = efeito_dados['descricao']
    linhas = textwrap.wrap(descricao, width=40)
    
    descricao = "\n".join(
        f"|    {linha:<42}|"
        for linha in linhas
    )
    if efeito_dados.get('duracao_turnos') is None:
        duracao = "perpétuo"
    else:
        duracao = f"{efeito_dados['duracao_turnos']} turnos"

    print(f"""
{linha}
|{efeito_dados["nome"]:^46}|
{linha}
|{"- Tipo:":<16}{efeito_dados['tipo']:<30}|
|{"- Duração:":<16}{duracao:<30}|
|{"- Dano_turno:":<16}{efeito_dados.get('dano_por_turno', "Sem dano"):<30}|
|{"- Cura_turno:":<16}{efeito_dados.get('cura_por_turno', "Sem cura"):<30}|
|{"- Modificador:":<16}{str(efeito_dados.get('modificador_dano', "0"))+"% de dano":<30}|
|{"- Descrição:":<46}|
{descricao}
{linha}
""")


def inspecionar_item(item):
    pass # no futuro faço varios itens separados em arma, equipamento e usavel, com varios atributos e efeitos

# inspecionar_habilidade("cura_forte")
# inspecionar_efeito("enfraquecido")

