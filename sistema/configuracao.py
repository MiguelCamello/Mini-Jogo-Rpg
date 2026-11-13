from interface.formatação import limpar_terminal, espacamento, normalizar_texto, slow_print, color_print
from interface.telas.menu import tela_config
from utils.resposta import verificar_resposta
from utils.carregar_json import CORES_JSON
from model.cores import cores_obj as c_obj
import json
import time

def configuracao():
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
                input(f"{c_obj.PRETO}[Voltar] {c_obj.RESET}")

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
                    slow_print(f"{cor} teve seu código alterado de {cores_dict[cor]} para {codigo} com sucesso!", cor=c_obj.VERDE)
                    time.sleep(1)

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
                slow_print("Configurações restauradas com sucesso!", cor=c_obj.VERDE)
                time.sleep(1)

                c_obj.atualizar()

            elif config == "4":
                break