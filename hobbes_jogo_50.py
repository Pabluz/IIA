import operator
import jogos_iia


class JogoHobbes(jogos_iia.Game):
    """Representação para o jogo:
    """
    ops = {"+": operator.add,
           "-": operator.sub}
    linhas = 5
    colunas = 5
    jogadores = ('rei_preto', 'rei_branco')
    conversor = {'p': 'rei_preto', 'b': 'rei_branco','n': None}

    # construtor do jogo hobbes
    def __init__(self):
        board = {(2, 1): 'n', (2, 2): 'n', (2, 4): 'n', (2, 5): 'n',
                 (3, 1): 'p', (3, 2): 'n', (3, 4): 'n', (3, 5): 'b',
                 (4, 1): 'n', (4, 2): 'n', (4, 4): 'n', (4, 5): 'n'}

        moves = [((3, 1), (2, 1)), ((3, 1), (3, 2)), ((3, 1), (4, 1))]
        self.initial = jogos_iia.GameState(self.jogadores[0], 0, (0, board), moves)

    @staticmethod
    def outro_jogador(j):
        return 'rei_preto' if j == 'rei_branco' else 'rei_branco'

    @staticmethod
    def conv_peca(j):
        return 'p' if j == 'rei_preto' else 'b'

    @staticmethod
    def outro_jogador_conv(j):
        return 'p' if j == 'b' else 'b'    

    @staticmethod
    def procura_jogador(tabuleiro, jogador):
        for key in tabuleiro.keys():
            if tabuleiro[key] == jogador:
                return key
        return None

    def do_actions(self, tabuleiro, jogador):

        jogador = self.conv_peca(jogador)
        adversario = self.conv_peca(self.outro_jogador(jogador))

        def gera_1a_parte(pos_rei, jogadas):  #FIXME:

            ja_passou = dict()

            for i in range(1, self.linhas + 1):
                for j in range(1, self.linhas + 1):
                    ja_passou[(j, i)] = False

            return generate_jogadas_1(ja_passou, pos_rei)

        def generate_jogadas_1(ja_passou, pos_rei):

            x = pos_rei[0]
            y = pos_rei[1]

            if (pos_rei not in tabuleiro and self.linhas >= x > 0 and self.linhas >= y > 0 and not ja_passou[pos_rei]) \
                or (pos_rei in tabuleiro and self.conversor[tabuleiro[pos_rei]] in (self.jogadores[0], self.jogadores[1])):
                ja_passou[pos_rei] = True
            else:
                return []

            return [pos_rei] + generate_jogadas_1(ja_passou, (x - 1, y)) + \
                   generate_jogadas_1(ja_passou, (x + 1, y)) + \
                   generate_jogadas_1(ja_passou, (x, y + 1)) + \
                   generate_jogadas_1(ja_passou, (x, y - 1))

        def gera_2a_jogada(pos_rei):

            x = pos_rei[0]
            y = pos_rei[1]

            jogadas = list()

            if (x - 1, y) in tabuleiro:
                if tabuleiro[(x - 1, y)] == adversario:
                    jogadas.append((x - 1, y))

                else:
                    push = push_jogada((x, y), 'X', '-')
                    pull = pull_jogada((x, y), 'X', '-')
                    jogadas.extend(push)
                    jogadas.extend(pull)

            if (x + 1, y) in tabuleiro:
                if tabuleiro[(x + 1, y)] == adversario:
                    jogadas.append((x + 1, y))

                else:
                    push = push_jogada((x, y), 'X', '+')
                    pull = pull_jogada((x, y), 'X', '+')
                    jogadas.extend(push)
                    jogadas.extend(pull)

            if (x, y + 1) in tabuleiro:
                if tabuleiro[(x, y + 1)] == adversario:
                    jogadas.append((x, y + 1))

                else:
                    push = push_jogada((x, y), 'Y', '+')
                    pull = pull_jogada((x, y), 'Y', '+')
                    jogadas.extend(push)
                    jogadas.extend(pull)

            if (x, y - 1) in tabuleiro:
                if tabuleiro[(x, y - 1)] == adversario:
                    jogadas.append((x, y - 1))

                else:
                    push = push_jogada((x, y), 'Y', '-')
                    pull = pull_jogada((x, y), 'Y', '-')
                    jogadas.extend(push)
                    jogadas.extend(pull)

            return [(pos_rei, jogada_2) for jogada_2 in jogadas]

        def push_jogada(pos_rei, eixo, op):
            func = self.ops[op]
            jogadas = list()

            x = pos_rei[0]
            y = pos_rei[1]

            if eixo == 'X':
                while (func(x, 2), y) not in tabuleiro and func(x, 2) > 0 and func(x, 2) <= 5:
                    x = func(x, 1)
                    jogadas.append((x, y))

            else:
                while (x, (func(y, 2))) not in tabuleiro and func(y, 2) > 0 and func(y, 2) <= 5:
                    y = func(y, 1)
                    jogadas.append((x, y))

            return jogadas

        def pull_jogada(pos_rei, eixo, op):
            func = self.ops[op]
            jogadas = list()

            x = pos_rei[0]
            y = pos_rei[1]

            if eixo == 'X':
                while (func(x, 1), y) not in tabuleiro and func(x, 1) > 0 and func(x, 1) <= 5:
                    x = func(x, 1)
                    jogadas.append((x, y))

            else:
                while (x, (func(y, 1))) not in tabuleiro and func(y, 1) > 0 and func(y, 1) <= 5:
                    y = func(y, 1)
                    jogadas.append((x, y))

            return jogadas

        pos_jogador = self.procura_jogador(tabuleiro, jogador)

        if pos_jogador is None:
            return []

        jogadas = gera_1a_parte(pos_jogador, [pos_jogador])
        jogadas_completo = list()

        for x in range(0, len(jogadas)):
            jogadas_completo.extend(gera_2a_jogada(jogadas[x]))
        print(jogadas_completo)
        return jogadas_completo

    # retorna jogadas possiveis de um dado estado
    def actions(self, state):
        return state.moves

    # retorna estado que se obtem a fazer uma jogada
    def result(self, state, move):
        jogada_1 = move[0]
        tabuleiro = state.board[1]
        jogador = self.conv_peca(state.to_move)

        tabuleiro_novo = dict(tabuleiro)

        # 1a jogada a fazer!
        pos_jogador = self.procura_jogador(tabuleiro_novo, jogador)

        del tabuleiro_novo[pos_jogador]
        tabuleiro_novo[jogada_1] = jogador
        # 1a jogada feita!

        # 2a jogada a fazer!
        jogada_2 = move[1]
        result = tuple(map(operator.sub, jogada_2, jogada_1))

        x = jogada_1[0]
        y = jogada_1[1]

        if jogada_2 in tabuleiro_novo and tabuleiro_novo[jogada_2] == self.outro_jogador(jogador):
            tabuleiro_novo[jogada_2] = jogador
            to_move_new = self.outro_jogador(state.to_move)
            moves_new = self.do_actions(tabuleiro_novo, to_move_new)
            utilidade_new = self.do_utility(tabuleiro_novo, to_move_new, moves_new)
            jogadas = state.board[0] + 1
            new_state = jogos_iia.GameState(to_move_new, utilidade_new, (jogadas, tabuleiro_novo), moves_new)
            return new_state

        moveu = 'x' if result[1] == 0 else 'y'
        del tabuleiro_novo[(x, y)]

        if (moveu == 'x'):
            if result[0] > 0:
                if (x + 1, y) in tabuleiro_novo:
                    del tabuleiro_novo[(x + 1, y)]
                    tabuleiro_novo[(jogada_2[0] + 1, y)] = 'n'
                else:
                    #del tabuleiro_novo[(x - 1, y)]
                    tabuleiro_novo[(jogada_2[0] - 1, y)] = 'n'
            else:
                if (x - 1, y) in tabuleiro_novo:
                    del tabuleiro_novo[(x - 1, y)]
                    tabuleiro_novo[(jogada_2[0] - 1, y)] = 'n'
                else:
                    #del tabuleiro_novo[(x + 1, y)]
                    tabuleiro_novo[(jogada_2[0] + 1, y)] = 'n'
        else:
            if result[1] > 0:
                if (x, y + 1) in tabuleiro_novo:
                    del tabuleiro_novo[(x, y + 1)]
                    tabuleiro_novo[(x, jogada_2[1] + 1)] = 'n'
                else:
                    #del tabuleiro_novo[(x, y - 1)]
                    tabuleiro_novo[(x, jogada_2[1] - 1)] = 'n'
            else:
                if (x, y - 1) in tabuleiro_novo:
                    del tabuleiro_novo[(x, y - 1)]
                    tabuleiro_novo[(x, jogada_2[1] - 1)] = 'n'
                else:
                    #del tabuleiro_novo[(x, y + 1)]
                    tabuleiro_novo[(x, jogada_2[1] + 1)] = 'n'

        tabuleiro_novo[jogada_2] = jogador
        # 2a jogada feita!
        to_move_new = self.outro_jogador(state.to_move)
        moves_new = self.do_actions(tabuleiro_novo, to_move_new)
        utilidade_new = self.do_utility(tabuleiro_novo, to_move_new, moves_new)
        jogadas = state.board[0] + 1
        new_state = jogos_iia.GameState(to_move_new, utilidade_new, (jogadas, tabuleiro_novo), moves_new)

        return new_state

    # Utilidade do estado, na perspectiva do jogador que tem a vez.  Rele-
    # vante apenas para os estados finais:  1, -1, ou 0, consoante seja de vitoria,
    # derrota ou empate.
    def do_utility(self, tabuleiro, jogador, moves):

        jog_peca = self.conv_peca(jogador)
        adv_peca = 'b' if jog_peca == 'p' else 'p'

        pos_jog = self.procura_jogador(tabuleiro, jog_peca)
        pos_peca = self.procura_jogador(tabuleiro, adv_peca)

        if pos_jog == None:
            return -1 if jogador == self.jogadores[0] else 1
        elif pos_peca == None:
            return 1 if jogador == self.jogadores[0] else -1

        if moves == []:
            return -1 if jogador == self.jogadores[0] else 1

        return 0

    def utility(self, state, jogador):

        return state.utility

    # metodo booleano que verific se um dado estado é final
    def terminal_test(self, state):
        return state.board[0] == 50 or state.utility

    # Mostra uma representação de um estado do jogo
    def display(self, state):

        tabuleiro = state.board[1]
        print("Tabuleiro actual:")
        print('-----------')
        for y in range(1, self.linhas + 1):
            print('|', end='')
            for x in range(1, self.colunas + 1):
                if (x, y) in tabuleiro:
                    if tabuleiro[(x, y)] == 'b':
                        print('b|', end='')
                    elif tabuleiro[(x, y)] == 'p':
                        print('p|', end='')
                    elif tabuleiro[(x, y)] == 'n':
                        print('n|', end='')
                else:
                    print(' |', end='')
            print('\n-----------')

        if self.terminal_test(state):
            print("Fim do jogo")
        else:
            print("Próximo jogador:{}\n".format(state.to_move))