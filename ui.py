"""
Módulo que faz a interface com o usuário
"""


from jogo_velha import *
from constantes import *
from termcolor import colored


def imprime_tabuleiro(tab):
    """
    Imprime um tabuleiro
    :param tab: o tabuleiro a ser impresso
    """
    for i in range(TAM_TAB):
        print("{} ".format(i+1), end=" ")
        for j in range(TAM_TAB):
            print(" {} ".format(tab[i][j]), end="")
            if j < TAM_TAB - 1:
                print("|", end="")
            else:
                print()
        if i < TAM_TAB - 1:
            print(ESPACO_3 + LINHA_HORIZONTAL)
    print(ESPACO_4 + "1" + ESPACO_3 + "2" + ESPACO_3 + "3")


def jogada_formato_valido(j):
    """
    Verifica se uma jogada tem um formato xy, onde x e y são números
    :param j: Um String que representa a jogada
    :return: True se o formato for válido ou False caso contrário
    """
    return j.isnumeric() and len(j) == 2


def recebe_jogada(t, tab):
    """
    Recebe uma jogada da entrada padrão
    :param t: O turno do jogador
    :param tab: O tabuleiro para que seja feita a impressão dele se o jogador não informar uma jogada válida
    :return: os valores x e y para indexar corretamente a matriz do tabuleiro
    """
    while True:
        print(colored("Jogador {}, é a sua vez!".format(t), "green"))
        print("Digite a jogada no formato xy, onde x é a linha e y a coluna:")
        jogada = input()
        if jogada_formato_valido(jogada):
            break
        print(colored("Jogada fora do formato correto!", "red"))
        imprime_tabuleiro(tab)
    return int(jogada[0])-1, int(jogada[1])-1


# Inicia o jogo
tabuleiro = constroi_tabuleiro()
turno = inicia_turno()

# Laço principal
while True:
    imprime_tabuleiro(tabuleiro)
    x, y = recebe_jogada(turno, tabuleiro)
    try:
        if joga(tabuleiro, turno, x, y):
            resultado = acabou(tabuleiro, turno)
            if resultado == JOG1 or resultado == JOG2 or resultado == EMPATE:
                break
            else:
                turno = troca_turno(turno)
        else:
            print(colored("Casa já está preenchida, escolha outra para jogar!", "red"))
    except ValueError:
        print(colored("A jogada tem que ser feita dentro do tabuleiro!", "red"))

imprime_tabuleiro(tabuleiro)
if resultado == EMPATE:
    print(colored("O jogo empatou!", "blue"))
else:
    print(colored("Jogador {} ganhou!".format(resultado), "blue"))
