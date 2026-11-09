from model.cores import cores_obj as c_obj


def tela_menu():

    linha, espaco = f"|{"="*32}|", f"|{" "*32}|"

    print(f"""
{" "*30}{linha}
{" "*30}|{"== RPG CAMELLO ==":^32}|
{" "*30}{linha}
{" "*30}{espaco}
{" "*30}{espaco}
{" "*30}|{" "*6}-[{c_obj.FUNDO_PRETO}{'Novo Jogo':^16}{c_obj.RESET}]-{" "*6}|
{" "*30}{espaco}
{" "*30}{espaco}
{" "*30}|{" "*6}-[{c_obj.FUNDO_PRETO}{'Carregar Jogo':^16}{c_obj.RESET}]-{" "*6}|
{" "*30}{espaco}
{" "*30}{espaco}
{" "*30}|{" "*6}-[{c_obj.FUNDO_PRETO}{'Configurações':^16}{c_obj.RESET}]-{" "*6}|
{" "*30}{espaco}
{" "*30}{espaco}
{" "*30}|{" "*6}-[{c_obj.FUNDO_PRETO}{'Creditos':^16}{c_obj.RESET}]-{" "*6}|
{" "*30}{espaco}
{" "*30}{espaco}
{" "*30}|{" "*6}-[{c_obj.FUNDO_PRETO}{'Sair':^16}{c_obj.RESET}]-{" "*6}|
{" "*30}{espaco}
{" "*30}{espaco}
{" "*30}{linha}
""")


def tela_config():
    cores_dict = c_obj.getAll_codigos()
    linha, espaco = f"|{"="*32}|", f"|{" "*32}|"

    print(f"""
{" "*30}{linha}
{" "*30}|{"== CONFIGURAÇÕES ==":^32}|
{" "*30}{linha}
{" "*30}{espaco}
{" "*30}|{'- ESQUEMA DE CORES -':^32}|
{" "*30}{espaco}
{" "*30}|{'-- Cores':^15}--{'Codigo --':^15}|
{" "*30}{espaco}
{" "*30}|{c_obj.PRETO}{" "*4}{'Preto':>8}{"--":^8}{('[ '+str(cores_dict['preto'])+' ]'):<8}{" "*4}{c_obj.RESET}|
{" "*30}|{c_obj.VERMELHO}{" "*4}{'Vermelho':>8}{"--":^8}{('[ '+str(cores_dict['vermelho'])+' ]'):<8}{" "*4}{c_obj.RESET}|
{" "*30}|{c_obj.DOURADO}{" "*4}{'Dourado':>8}{"--":^8}{('[ '+str(cores_dict['dourado'])+' ]'):<8}{" "*4}{c_obj.RESET}|
{" "*30}|{c_obj.VERDE}{" "*4}{'Verde':>8}{"--":^8}{('[ '+str(cores_dict['verde'])+' ]'):<8}{" "*4}{c_obj.RESET}|
{" "*30}|{c_obj.AZUL}{" "*4}{'Azul':>8}{"--":^8}{('[ '+str(cores_dict['azul'])+' ]'):<8}{" "*4}{c_obj.RESET}|
{" "*30}|{c_obj.ROXO}{" "*4}{'Roxo':>8}{"--":^8}{('[ '+str(cores_dict['roxo'])+' ]'):<8}{" "*4}{c_obj.RESET}|
{" "*30}{espaco}
{" "*30}|{'[1] Teste de cores ':^32}|
{" "*30}|{'[2] Mapear as cores':^32}|
{" "*30}|{'[3] Restaurar padrão':^32}|
{" "*30}|{'[4] Voltar':^32}|
{" "*30}{espaco}
{" "*30}{linha}
""")


def tela_creditos():

    linha, espaco = f"|{"="*32}|", f"|{" "*32}|"

    print(f"""
{" "*30}{linha}
{" "*30}|{"== Creditos ==":^32}|
{" "*30}{linha}
{" "*30}|{"- Diretor do Projeto -":^32}|
{" "*30}|{c_obj.PRETO}{"Miguel de Lima Camello":^32}{c_obj.RESET}|
{" "*30}{espaco}
{" "*30}|{"- Desenvolvedor Back-end -":^32}|
{" "*30}|{c_obj.VERMELHO}{"Miguel de Lima Camello":^32}{c_obj.RESET}|
{" "*30}{espaco}
{" "*30}|{"- Desenvolvedor Front-end -":^32}|
{" "*30}|{c_obj.DOURADO}{"Miguel de Lima Camello":^32}{c_obj.RESET}|
{" "*30}{espaco}
{" "*30}|{"- Desenvolvedor Database -":^32}|
{" "*30}|{c_obj.VERDE}{"Miguel de Lima Camello":^32}{c_obj.RESET}|
{" "*30}{espaco}
{" "*30}|{"- Tester de Qualidade -":^32}|
{" "*30}|{c_obj.AZUL}{"Miguel de Lima Camello":^32}{c_obj.RESET}|
{" "*30}{espaco}
{" "*30}|{"- Special Thanks! -":^32}|
{" "*30}|{c_obj.ROXO}{"Miguel de Lima Camello":^32}{c_obj.RESET}|
{" "*30}{linha}
""")
