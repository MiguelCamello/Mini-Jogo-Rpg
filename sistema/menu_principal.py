from interface.formatação import limpar_terminal, espacamento, normalizar_texto, slow_print, color_print
from interface.telas.menu import tela_creditos, tela_menu
from sistema.configuracao import configuracao
from utils.resposta import verificar_resposta
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

        if acao == "jogar":
            return

        if acao in ["configuracao", "configuracoes"]:
            configuracao()

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
