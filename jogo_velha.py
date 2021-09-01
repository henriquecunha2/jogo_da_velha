"""
Esse módulo prvê funções para levar a efeito um jogo da velha.
A interface deve usar essas funções para:
- Operar sobre o tabuleiro
- Operar sobre o turno dos jogadores
- Garantir as condições iniciais do jogo
- Verificar as condições de término do jogo
"""

from constantes import *
from random import randint


def constroi_tabuleiro():
    """
    Constroi um tabuleiro em formato de uma matriz de ordem constantes.TAM_TAB
    :return: Uma matriz que representa o tabuleiro
    """
    tab = []
    for i in range(TAM_TAB):
        tab.append([])
        for j in range(TAM_TAB):
            tab[i].append(CASA_VAZIA)
    return tab


def inicia_turno():
    """
    Escohe um jogador aleatoriamente para iniciar a partida
    :return: JOG1 ou JOG2 aleatoriamente
    """
    dado = randint(0, 1)
    if dado == 0:
        return JOG1
    else:
        return JOG2


def jogada_valida(x, y):
    """
    Verifica se a jogada cai dentro do tabuleiro
    :param x: A linha no tabuleiro onde a jogada deve ser feita
    :param y: A coluna no tabuleiro onde a jogada deve ser feita
    :return: True se a jogada foi feita para dentro do tabuleiro ou False para fora do tabuleiro
    """
    return 0 <= x < TAM_TAB and 0 <= y < TAM_TAB


def joga(tabuleiro, turno, x: int, y: int):
    """
    Realiza uma jogada do jogador da vez. Se a jogada for para fora do tabuleiro, lança uma exceção.
    :param tabuleiro: O tabuleiro sobre o qual deve ser feita a jogada
    :param turno: O jogador da vez
    :param x: A linha no tabuleiro onde a jogada deve ser feita
    :param y: A coluna no tabuleiro onde a jogada deve ser feita
    :return: True se a jogada foi feita com sucesso ou False se a casa do tabuleiro já estava ocupada
    :raises: ValueError se a jogada for para fora do tabuleiro
    """
    if not jogada_valida(x, y):
        raise ValueError("Jogada fora do tabuleiro")

    if tabuleiro[x][y] == CASA_VAZIA:
        tabuleiro[x][y] = turno
        return True
    return False


def troca_turno(turno):
    """
    Troca o turno dos jogadores
    :param turno: Um string que representa o jogador atual
    :return: Um string que representa o outro jogador para o qual o turno vai ser trocado
    """
    if turno == JOG1:
        return JOG2
    else:
        return JOG1


def acabou(tabuleiro, turno):
    """
    Verifica se o jogo acabou e quem fi o vencedor ou seu deu empate.
    :param tabuleiro: O tabuleiro sobre o qual deve ser feita a verificação
    :param turno: O jogador que realizou a última jogada
    :return: EMPATE se a partida terminou empatada, JOG1 se o jogador 1 venceu ou JOG2 se o jogador 2 venceu
    """
    ganhou_diag_principal = 0
    ganhou_diag_secundaria = 0
    for i in range(TAM_TAB):
        ganhou_linha = 0
        ganhou_coluna = 0
        for j in range(TAM_TAB):
            if tabuleiro[i][j] == turno:
                ganhou_linha += 1
            if tabuleiro[j][i] == turno:
                ganhou_coluna += 1
        if ganhou_linha == TAM_TAB or ganhou_coluna == TAM_TAB:
            return turno

        if tabuleiro[i][i] == turno:
            ganhou_diag_principal += 1
        if tabuleiro[i][TAM_TAB-1-i] == turno:
            ganhou_diag_secundaria += 1

    if ganhou_diag_principal == TAM_TAB or ganhou_diag_secundaria == TAM_TAB:
        return turno

    empatou = True
    for i in range(TAM_TAB):
        for j in range(TAM_TAB):
            if tabuleiro[i][j] == CASA_VAZIA:
                empatou = False

    if empatou:
        return EMPATE

    return False
