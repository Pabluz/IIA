import jogar
import hobbes_jogo_50

jogo_hobbes = hobbes_jogo_50.JogoHobbes()

j1 = jogar.Jogador(jogo_hobbes,"Ze",f = jogar.random_player)
j2 = jogar.Jogador(jogo_hobbes,"Ao Calhas",f = jogar.random_player)

result = jogar.um_jogo(jogo_hobbes,j1,j2,0,True)

print(result)
