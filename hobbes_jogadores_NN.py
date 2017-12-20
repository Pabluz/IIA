def f_aval_peoes_F1(estado, jogador):
    adversario = peoes_jogo.JogoPeoes.outro_jogador(jogador)
    if vitoria_3peoes(jogador, estado):
        f = 2
    elif vitoria_3peoes(adversario, estado):
        f = -2
    else:
        f = len(estado.board[jogador]) - len(estado.board[adversario])
    return f


def jogador_2peoes_F1(jogo, estado, nivel=5):
    return jogos_iia.alphabeta_cutoff_search(estado, jogo, nivel, eval_fn=f_aval_peoes_F1)