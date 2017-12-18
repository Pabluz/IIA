
import operator
import jogos_iia

class JogoHobbes(jogos_iia.Game) :
    """Representação para o jogo:
    """
    ops = {"+": operator.add,
           "-": operator.sub}
    linhas = 5
    colunas = 5
    jogadores = ('rei_preto,rei_branco')


    @staticmethod
    def outro_jogador(j) :
        return 'rei_preto' if j == 'rei_branco' else 'rei_preto'

    #construtor do jogo hobbes
    def _init_(self):
        return

    @staticmethod
    def conv_peca(j):
        return 'p' if j == 'p' else 'b'

    @staticmethod
    def conv_pecinha(j):
        return 'p' if j == 'rei_preto' else 'b'

    @staticmethod
    def procura_jogador(tabuleiro, jogador):
        for key in tabuleiro.keys():
            if tabuleiro[key] == jogador:
                return key

    #retorna jogadas possiveis de um dado estado
    def actions(self, state):

        tabuleiro = state.board[1] #atribuicao do tabuleiro

        jogador = state.to_move
        if jogador == 'rei_branco':
            jogador = 'b'
            outro_jogador = 'p'
        else:
            jogador = 'p'
            outro_jogador = 'b'

        def gera_1a_parte( pos_rei, jogadas):

            x = pos_rei[0]
            y = pos_rei[1]

            ja_passou = dict()

            for i in range(1, 6):
                for j in range(1, 6):
                    ja_passou[(i, j)] = False

            ja_passou[(x, y)] = True

            generate_jogadas_1(ja_passou, pos_rei, jogadas)

            return jogadas

        def generate_jogadas_1(ja_passou, pos_rei, jogadas):

            x = pos_rei[0]
            y = pos_rei[1]

            if (x - 1, y) not in tabuleiro and x-1 > 0 and not (ja_passou[(x - 1, y)]) :
                jogadas.append((x - 1, y))
                ja_passou[(x - 1, y)] = True
                jogadas.extend(generate_jogadas_1(ja_passou, (x - 1, y), jogadas))

            if (x + 1, y) not in tabuleiro and x + 1 <= self.colunas and not(ja_passou[(x + 1, y)]):
                jogadas.append((x + 1, y))
                ja_passou[(x + 1, y)] = True
                jogadas.extend(generate_jogadas_1(ja_passou, (x + 1, y), jogadas))
            if (x, y + 1) not in tabuleiro and y + 1 <= self.colunas and not (ja_passou[(x, y + 1)]):
                jogadas.append((x, y + 1))
                ja_passou[(x, y + 1)] = True
                jogadas.extend(generate_jogadas_1(ja_passou, (x, y + 1), jogadas))
            if (x, y - 1) not in tabuleiro and y-1 > 0 and not (ja_passou[(x, y - 1)]):
                jogadas.append((x, y - 1))
                ja_passou[(x, y - 1)] = True
                jogadas.extend(generate_jogadas_1(ja_passou, (x, y - 1), jogadas))

            return jogadas

        def gera_2a_jogada(pos_rei):

            x = pos_rei[0]
            y = pos_rei[1]

            jogadas = list()

            if (x - 1, y) in tabuleiro:
                if tabuleiro [(x - 1, y)] == outro_jogador:
                    jogadas.append((x - 1, y))

                else:
                    push = push_jogada((x , y),'X','-')
                    pull = pull_jogada((x , y), 'X','-')
                    jogadas.extend(push)
                    jogadas.extend(pull)

            if (x + 1, y) in tabuleiro:
                if tabuleiro[(x + 1, y)] == outro_jogador:
                    jogadas.append((x + 1, y))

                else:
                    push = push_jogada((x, y), 'X', '+')
                    pull = pull_jogada((x, y), 'X', '+')
                    jogadas.extend(push)
                    jogadas.extend(pull)

            if (x, y + 1) in tabuleiro:
                if tabuleiro[(x, y + 1)] == outro_jogador:
                    jogadas.append((x, y + 1))

                else:
                    push = push_jogada((x, y), 'Y', '+')
                    pull = pull_jogada((x, y), 'Y', '+')
                    jogadas.extend(push)
                    jogadas.extend(pull)

            if (x, y - 1) in tabuleiro:
                if tabuleiro[(x, y - 1)] == outro_jogador:
                    jogadas.append((x, y - 1))

                else:
                    push = push_jogada((x, y), 'Y', '-')
                    pull = pull_jogada((x, y), 'Y', '-')
                    jogadas.extend(push)
                    jogadas.extend(pull)

            return [(pos_rei,jogada_2) for jogada_2 in jogadas]

        def push_jogada(pos_rei, eixo,op):
            func = self.ops[op]
            jogadas = list()

            x = pos_rei[0]
            y = pos_rei[1]

            if eixo == 'X':
                while (func(x,2), y) not in tabuleiro and func(x,2) >0 and func(x,2) <= 5:
                    x = func(x, 1)
                    jogadas.append((x,y))

            else:
                while (x, (func(y, 2))) not in tabuleiro and func(y,2) >0 and func(y,2) <= 5:
                    y = func(y, 1)
                    jogadas.append((x,y))

            return jogadas


        def pull_jogada(pos_rei, eixo,op):
            func = self.ops[op]
            jogadas = list()

            x = pos_rei[0]
            y = pos_rei[1]

            if eixo == 'X':
                while (func(x, 1), y) not in tabuleiro and func(x,1) >0 and func(x,1) <= 5:
                    x = func(x, 1)
                    jogadas.append((x,y))

            else:
                while (x, (func(y, 1))) not in tabuleiro and func(y,1) >0 and func(y,1) <= 5:
                    y = func(y, 1)
                    jogadas.append((x,y))

            return jogadas

        pos_jogador = self.procura_jogador(tabuleiro, jogador)

        jogadas = gera_1a_parte(pos_jogador, [pos_jogador])
        jogadas_completo = list()

        for x in range(0, len(jogadas)):
            jogadas_completo.extend(gera_2a_jogada(jogadas[x]))

        return jogadas_completo


    #retorna estado que se obtem a fazer uma jogada
    def result(self, state, move):
        jogada_1 = move[0]
        tabuleiro = state.board[1]
        jogador = self.conv_pecinha(state.to_move)

        #1a jogada a fazer!
        pos_jogador = self.procura_jogador(tabuleiro, jogador)

        del tabuleiro[pos_jogador]
        tabuleiro[jogada_1] = jogador
        #1a jogada feita!
        
        #2a jogada a fazer!
        jogada_2 = move[1]
        result = tuple(map(operator.sub, jogada_2, jogada_1))

        x = jogada_1[0]
        y = jogada_1[1]

        if tabuleiro[jogada_2] == self.outro_jogador(jogador):
            tabuleiro[jogada_2] = jogador
            return state
        
        moveu = 'x' if result[1] == 0 else 'y'

        if(moveu == 'x'):
            if (x - 1, y) in tabuleiro:
                del tabuleiro[(x-1,y)]
                tabuleiro[(jogada_2[0]-1,y)] = 'n'
            elif (x + 1, y) in tabuleiro:
                del tabuleiro[(x+1,y)]
                tabuleiro[(jogada_2[0]+1,y)] = 'n'
        else:           
            if (x, y-1) in tabuleiro:
                del tabuleiro[(x,y-1)]
                tabuleiro[(x,jogada_2[1]-1)] = 'n'
            elif (x, y+1) in tabuleiro:
                del tabuleiro[(x,y+1)]
                tabuleiro[(x,jogada_2[1]+1)] = 'n'

        tabuleiro[jogada_2] = jogador
        #2a jogada feita!
        state.to_move = self.outro_jogador(state.to_move)

        return state

    # Utilidade do estado, na perspectiva do jogador que tem a vez.  Rele-
    # vante apenas para os estados finais:  1, -1, ou 0, consoante seja de vitoria,
    # derrota ou empate.
    def utility(self, state, jogador):

        jog_peca = self.conv_peca(jogador)
        adv_peca = 'b' if jog_peca == 'p' else 'p'

        tabuleiro = state.board[1]
        string = ''
        concat = ''

        for x in range(1, self.linhas + 1):
            for y in range(1, self.colunas + 1):
                if tabuleiro[(x, y)] == 'b':
                    string = 'b'
                if tabuleiro[(x, y)] == 'p':
                    string = 'p'
                if string != '':
                    concat = concat + string
                    string = ''

        if concat == jog_peca:
            return 1
        elif concat == adv_peca:
            return -1
        else:
            return 0

    # metodo booleano que verific se um dado estado é final
    def terminal_test(self, state):
        return self. actions(state) == [] or state.board[0] == 50 or self.utility(state, 'rei_preto') != 0

    # Mostra uma representação de um estado do jogo
    def display(self, state):

        tabuleiro = state.board[1]
        print("Tabuleiro actual:")
        for x in range(1, self.linhas + 1):
            print('|', end='')
            for y in range(1, self.colunas + 1):
                if(x, y) in tabuleiro:
                    if tabuleiro[(x, y)] == 'b':
                        print('b|', end='')
                    elif tabuleiro[(x, y)] == 'p':
                        print('p|', end='')
                    elif tabuleiro[(x, y)] == 'n':
                        print('n|', end='')
                else:
                     print(' |', end='')
            print('\n -----------',)

       # if self.terminal_test(state):
        #    print("Fim do jogo")
        else:
            print("Próximo jogador:{}\n".format(state.to_move))