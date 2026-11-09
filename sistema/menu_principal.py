from interface.formatação import limpar_terminal, espacamento, normalizar_texto, slow_print, color_print
from interface.telas.menu import tela_config, tela_creditos, tela_menu
from utils.resposta import verificar_resposta
from utils.carregar_json import CORES_JSON
from model.cores import cores_obj as c_obj
import json
import time
import sys


def menu_principal():
    menu_aberto = True
    while menu_aberto:
        limpar_terminal()

        tela_menu()

        espacamento(30)
        slow_print("O'que deseja fazer?")

        espacamento(30)
        acao = normalizar_texto(input(" > "))

        if acao in ["novo_jogo", "carregar_jogo"]:
            return acao

        if acao in ["configuracao", "configuracoes"]:
            while True:
                limpar_terminal()

                tela_config()

                espacamento(30)
                slow_print("O'que deseja configurar?")
                espacamento(30)
                config = normalizar_texto(input(" > "))

                if config == "1":
                    limpar_terminal()

                    c_obj.teste_de_cores()

                    print()
                    slow_print(
                        f"{c_obj.VERMELHO}Atenção!{c_obj.RESET} as cores podem ser diferentes para cada terminal e computador!")
                    input("[Voltar] ")

                elif config == "2":
                    while True:
                        limpar_terminal()

                        espacamento(30)
                        print(f"{c_obj.PRETO}Preto, {c_obj.VERMELHO}Vermelho, {c_obj.DOURADO}Dourado, {c_obj.VERDE}Verde, {c_obj.AZUL}Azul, {c_obj.ROXO}Roxo{c_obj.RESET}")
                        espacamento(30)
                        slow_print("Qual cor deseja alterar? [Voltar]")

                        espacamento(30)
                        cor = normalizar_texto(input(" > "))

                        if cor == "voltar":
                            break

                        cores_dict = c_obj.getAll_codigos()

                        if cor not in cores_dict:
                            color_print(f"{cor} não é uma cor valida no terminal!")
                            time.sleep(2)
                            continue

                        espacamento(30)
                        slow_print(f"{cor}: {cores_dict[cor]}")
                        espacamento(30)
                        slow_print("Qual codigo de cor, você quer que sobrepuje o original?")

                        espacamento(30)
                        codigo = int(input(" > "))
                        if codigo == str:
                            color_print(
                                "O código deve ser um numero não um texto!")
                            continue

                        with open(CORES_JSON, "r", encoding="utf-8") as arquivo_cores:
                            cores_json = json.load(arquivo_cores)

                            cores_json["cores"][cor] = codigo

                        with open(CORES_JSON, "w", encoding="utf-8") as arquivo_cores:
                            json.dump(cores_json, arquivo_cores,
                                    indent=4, ensure_ascii=False)

                        espacamento(30)
                        slow_print(
                            f"{cor} teve seu código alterado de {cores_dict[cor]} para {codigo} com sucesso!")

                        c_obj.atualizar()
                        break

                elif config == "3":
                    limpar_terminal()

                    espacamento(30)
                    slow_print("Deseja restaurar as configurações ao estado original?")

                    espacamento(30)
                    restaurar = normalizar_texto(input(" > "))

                    if not verificar_resposta(restaurar):
                        break

                    with open(CORES_JSON, "r", encoding="utf-8") as arquivo_cores:
                        cores_json = json.load(arquivo_cores)
                
                        cores_json['cores'] = cores_json['cores_backup'].copy()
                
                    with open(CORES_JSON, "w", encoding="utf-8") as arquivo_cores:
                        json.dump(cores_json, arquivo_cores, indent=4, ensure_ascii=False)
                        
                    espacamento(30)
                    slow_print("Configurações restauradas com sucesso!")

                    c_obj.atualizar()

                elif config == "4":
                    break

        elif acao in ["creditos", "credito"]:
            limpar_terminal()

            tela_creditos()

            espacamento(30)
            input("[Voltar] ")

        elif acao == "sair":
            limpar_terminal()

            espacamento(30)
            slow_print("Tem certeza que deseja sair do jogo?")

            espacamento(30)
            sair = normalizar_texto(input(" > "))

            if sair == "sou_dev":
                limpar_terminal()
                sys.exit()

            if not verificar_resposta(sair):
                continue

            limpar_terminal()

            espacamento(30)
            slow_print("É um jogo muuito bom e divertido!", end="\n\n")

            espacamento(30)
            slow_print(
                "Os produtores são ótimos, da uma olhada nos creditos!", end="\n\n")

            espacamento(30)
            slow_print("Tem certeza que deseja perder essa experiência???")

            espacamento(30)
            sair = normalizar_texto(input(" > "))

            if not verificar_resposta(sair):
                continue

            limpar_terminal()

            espacamento(30)
            slow_print(
                "É um joginho de turno em python, estilo pokemon", end="\n\n")

            espacamento(30)
            slow_print(
                "Temos UIs bem feitas e pensadas pelo nosso dev Front-end", end="\n\n")

            espacamento(30)
            slow_print(
                "Temos lutas e combate otimos desenvolvido pelo nosso dev Back-end", end="\n\n")

            espacamento(30)
            slow_print(
                "Seu progresso fica salvo graças ao nosso dev Database", end="\n\n")

            espacamento(30)
            slow_print(
                "Tudo isso foi testado pelo nosso Tester especial para melhor experiência do usuario!", end="\n\n")

            espacamento(30)
            slow_print("Deseja mesmo sair dessa obra prima?")

            espacamento(30)
            sair = normalizar_texto(input(" > "))

            if not verificar_resposta(sair):
                continue
            else:
                limpar_terminal()
                espacamento(30)
                slow_print("Ok ):", delay=0.5)
                sys.exit()
