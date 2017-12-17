
import operator

class JogoHobbes(jogos_iia.Game) :
    """Representação para o jogo:
    """
    ops = {"+": operator.add,
           "-": operator.sub,
           "*": operator.mul,
           "/": operator.div}



    @staticmethod
    def outro_jogador(j) :
        return 'rei_preto' if j == 'rei_branco' else 'rei_preto'


    #construtor do jogo hobbes
    def _init_(self):
        return null


    #retorna jogadas possiveis de um dado estado
    def actions(self, state):
        def gera_1a_parte(tabuleiro, pos_rei, jogadas):

            x = pos_rei[0]
            y = pos_rei[1]

            ja_passou = dict()

            for (i in range(1, 6))
                for (j in range(1, 6))
                    ja_passou[(i, j)] = False

            ja_passou[(x, y)] = True

            generate_jogadas_1(self, ja_passou, pos_rei, jogadas,tabuleiro)

            return jogadas

        def generate_jogadas_1(self, ja_passou, pos_rei, jogadas, tabuleiro):

            x = pos_rei[0]
            y = pos_rei[1]

            if (x - 1, y) not in tabuleiro and ja_passou[(x - 1, y)] == False:
                jogadas.append((x - 1, y))
                ja_passou[(x - 1, y)] = True
                jogadas.extend(generate_jogadas_1(ja_passou, (x - 1, y), jogadas, tabuleiro))

            if (x + 1, y) not in tabuleiro and ja_passou[(x + 1, y)] == False:
                jogadas.append((x + 1, y))
                ja_passou[(x + 1, y)] = True
                jogadas.extend(generate_jogadas_1(ja_passou, (x + 1, y), jogadas, tabuleiro))
            if (x, y + 1) not  in tabuleiro and ja_passou[(x, y + 1)] == False:
                jogadas.append((x, y + 1))
                ja_passou[(x, y + 1)] = True
                jogadas.extend(generate_jogadas_1(ja_passou, (x, y + 1), jogadas, tabuleiro))
            if (x, y - 1) not in tabuleiro and ja_passou[(x, y - 1)] == False:
                jogadas.append((x, y - 1))
                ja_passou[(x, y - 1)] = True
                jogadas.extend(generate_jogadas_1(ja_passou, (x, y - 1), jogadas, tabuleiro))

            return jogadas

        def gera_2a_jogada(self, tabuleiro, pos_rei, jogador):


            jogadas = list()

            if (x - 1, y) in tabuleiro:
                push = push_jogada(tabuleiro, (x , y)),'X','-')
                pull = pull_jogada(tabuleiro, (x , y), 'X','-')
                jogadas.extend(push)
                jogadas.extend(pull)

                if (x + 1, y) in tabuleiro:
                    actions.append("Baixo")
                if (x, y + 1) in tabuleiro:
                    actions.append("Direita")
                if (x, y - 1) in tabuleiro:
                    actions.append("Esquerda")

        def push_jogada(tabuleiro, pos_rei, eixo,op):
            func = ops[op]
            jogadas = list()

            x = pos_rei[0]
            y = pos_rei[1]

            if(eixo = 'X')
                while ((func(x,2), y) not in tabuleiro)
                    jogadas.append(pos_rei)
            else
                while (x, (func(y, 2)) not in tabuleiro)


        def pull_jogada(tabuleiro, jogada)
        tabuleiro = state.board
        jogador = state.to_move
        if jogador == 'rei_branco':
            jogador = 'b'
        else
            jogador = 'p'

        pos_jogador = tabuleiro[jogador]
        jogadas_= gera_1a_parte(tabuleiro,  pos_jogador, list(pos_jogador))

        jogadas_completo = list()

        for (x in in range(0, len(jogadas)))
            jogadas_completo.extend(gera_2a_jogada(self, tabuleiro, x, jogador))

        return jogadas_completo


    #retorna estado que se obtem a fazer uma jogada
    def result(self, state,move):
        return null

    # Cálculo da utilidade de um estado na perspectiva de um dado jogador.
    # Deverá ter o valor 1, para o caso de vitória, ou -1 em caso de derrota.
    def utility(self, state, jogador):
        final = 0
        adversario = JogoHobbes.outro_jogador(jogador)

        return final

    # metodo booleano que verific se um dado estado é final
    def terminal_test(self, state):
        return null

    # Mostra uma representação de um estado do jogo
    def display(self, state):

        tabuleiro = state.board
        print("Tabuleiro actual:")
        for x in range(1, self.linhas + 1):
            print('|')
            for y in range(1, self.colunas + 1):

                if board[(x, y)] == 'b':
                    print('b|')
                elif board[(x, y)] == 'p':
                    print('p|')
                elif board[(x, y)] == 'n':
                    print('n|')
                else:
                    print(' ')
            print('|')
            print('\n -----------')

        if self.terminal_test(state):
            print("Fim do jogo")
        else:
            print("Próximo jogador:{}\n".format(state.to_move))









