import hobbes_jogo_50

def f_numero_jogadas_possiveis(state): #quanto mais, melhor
    return len(state.moves)

def f_ataque(state, jogador): #quanto mais, melhor
    jog = JogoHobbes.conv_peca(jogador)
    y_jog = JogoHobbes.procura_jogador(state, jog)[1]
    if jogador == 'rei_preto':
        return abs(5-y_jog)
    else:
        return abs(1-y_jog)

def f_defesa(state, jog): #quanto mais, pior
    jog = JogoHobbes.conv_peca(jogador)
    x_jog = JogoHobbes.procura_jogador(state, jog)[0]
    return -abs(3-x_jog)

def f_distancia_reis(state, jog): #quanto mais, melhor
    jog = JogoHobbes.conv_peca(jogador)
    adv = JogoHobbes.outro_jogador_conv(jog)
    (x_jog,y_jog) = JogoHobbes.procura_jogador(state, jog)
    (x_adv,y_adv) = JogoHobbes.procura_jogador(state, adv)
    return (((x_jog - x_adv)**2)+((y_jog - y_adv)**2))**(0.5)

def f_prisao(state, jogador): #quanto mais, pior
    jog = JogoHobbes.conv_peca(jogador)

    def conta_barreiras(state, jog):
        (x_jog,y_jog) = procura_jogador(state, jog)
        soma = 0
        tabuleiro = state.board[1]
        if((x_jog+1 > 5) or \
            ((x_jog+1,y_jog) in tabuleiro and \
            tabuleiro[(x_jog+1,y_jog)] == 'n')):
            soma++
        if((x_jog-1 < 1) or \
            ((x_jog-1,y_jog) in tabuleiro and \
            tabuleiro[(x_jog-1,y_jog)] == 'n')):
            soma++
        if((y_jog+1 > 5) or \
            ((x_jog,y_jog+1) in tabuleiro and \
            tabuleiro[(x_jog,y_jog+1)] == 'n')):
            soma++
        if((y_jog-1 < 1) or \
            ((x_jog,y_jog-1) in tabuleiro and \
            tabuleiro[(x_jog,y_jog-1)] == 'n')):
            soma++
        return soma
    
    return conta_barreiras(state, jog)
   