import hobbes_jogo_50
import jogos_iia

def f_numero_jogadas_possiveis(state, jogador): #quanto mais, melhor
    return len(state.moves)

def f_ataque(state, jogador): #quanto mais, melhor
    tabuleiro = state.board[1]
    jog = hobbes_jogo_50.JogoHobbes.conv_peca(jogador)
    y_jog = hobbes_jogo_50.JogoHobbes.procura_jogador(tabuleiro, jog)[1]
    if jogador == 'rei_preto':
        return abs(5-y_jog)
    else:
        return abs(1-y_jog)

def f_defesa(state, jog): #quanto mais, pior
    tabuleiro = state.board[1]
    jog = hobbes_jogo_50.JogoHobbes.conv_peca(jog)
    x_jog = hobbes_jogo_50.JogoHobbes.procura_jogador(tabuleiro, jog)[0]
    return -abs(3-x_jog)

def f_distancia_reis(state, jog): #quanto mais, melhor
    tabuleiro = state.board[1]
    jog = hobbes_jogo_50.JogoHobbes.conv_peca(jog)
    adv = hobbes_jogo_50.JogoHobbes.outro_jogador_conv(jog)
    (x_jog,y_jog) = hobbes_jogo_50.JogoHobbes.procura_jogador(tabuleiro, jog)
    (x_adv,y_adv) = hobbes_jogo_50.JogoHobbes.procura_jogador(tabuleiro, adv)

    if x_jog == -1 or x_adv == -1:
        return -1500 if x_jog == -1 else 1500

    return (((x_jog - x_adv)**2)+((y_jog - y_adv)**2))**(0.5)

def f_prisao(state, jogador): #quanto mais, pior
    jog = hobbes_jogo_50.JogoHobbes.conv_peca(jogador)

    def conta_barreiras(state, jog):
        tabuleiro = state.board[1]
        (x_jog,y_jog) = hobbes_jogo_50.JogoHobbes.procura_jogador(tabuleiro, jog)
        soma = 0
        if((x_jog+1 > 5) or \
            ((x_jog+1,y_jog) in tabuleiro and \
            tabuleiro[(x_jog+1,y_jog)] == 'n')):
            soma = soma + 1
        if((x_jog-1 < 1) or \
            ((x_jog-1,y_jog) in tabuleiro and \
            tabuleiro[(x_jog-1,y_jog)] == 'n')):
            soma = soma + 1
        if((y_jog+1 > 5) or \
            ((x_jog,y_jog+1) in tabuleiro and \
            tabuleiro[(x_jog,y_jog+1)] == 'n')):
            soma = soma + 1
        if((y_jog-1 < 1) or \
            ((x_jog,y_jog-1) in tabuleiro and \
            tabuleiro[(x_jog,y_jog-1)] == 'n')):
            soma = soma + 1
        return soma
    
    return -conta_barreiras(state, jog)
def f_misto(state, jogador): #quanto mais, pior
    return 0.8*f_distancia_reis(state, jogador) +0.2*f_prisao(state, jogador)

def jogador_numero_jogadas_possiveis(jogo,estado, nivel = 5) :
    return jogos_iia.alphabeta_cutoff_search(estado,jogo,nivel,eval_fn = f_misto)
def jogador_ataque(jogo,estado, nivel = 5) :
    return jogos_iia.alphabeta_cutoff_search(estado,jogo,nivel,eval_fn = f_defesa)
def jogador_defesa(jogo,estado, nivel = 5) :
    return jogos_iia.alphabeta_cutoff_search(estado,jogo,nivel,eval_fn = f_numero_jogadas_possiveis)
def jogador_distancia_reis(jogo,estado, nivel = 5) :
    return jogos_iia.alphabeta_cutoff_search(estado,jogo,nivel,eval_fn =  f_prisao)
def jogador_prisao(jogo,estado, nivel = 5) :
    return jogos_iia.alphabeta_cutoff_search(estado,jogo,nivel,eval_fn =  f_prisao)
def jogador_mista(jogo,estado, nivel = 5) :
    return jogos_iia.alphabeta_cutoff_search(estado,jogo,nivel,eval_fn =  f_mista)