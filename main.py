# -*- coding: utf-8 -*-
## Main - Jogo dos Peões

#Módulos genéricos
import jogar     # utlidades para realizar jogos

# Módulos específicos do jogo dos peões
import hobbes_jogo_NN
import jogos_iia


board = {(2, 1): 'n', (2, 2): 'n', (2, 4): 'n', (2, 5): 'n',
(3, 1): 'p', (3, 2): 'n', (3, 4): 'n', (3, 5): 'b',
(4, 1): 'n', (4, 2): 'n', (4, 4): 'n', (4, 5): 'n'}

moves = [((3,1),(2,1)),((3,1),(3,2)),((3,1),(4,1))]

state = jogos_iia.GameState('rei_preto',0,(0,board),moves)

jogo_hobbes =hobbes_jogo_NN.JogoHobbes()

print (jogo_hobbes.display(state))

print(jogo_hobbes.actions(state))


