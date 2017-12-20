import jogar
import hobbes_jogo_50
import hobbes_jogadores_50

jogo_hobbes = hobbes_jogo_50.JogoHobbes()

j1 = jogar.Jogador(jogo_hobbes,"Ze",f = jogar.random_player)
j2 = jogar.Jogador(jogo_hobbes,"Ao Calhas",f =hobbes_jogadores_50.jogador_numero_jogadas_possiveis )
j3 = jogar.Jogador(jogo_hobbes,"Campeao",f =hobbes_jogadores_50.jogador_ataque)
#hobbes_jogadores_50.jogador_numero_jogadas_possiveis
result = jogar.n_pares_de_jogos(jogo_hobbes,10,j1,j2,3,False)

print(result)
