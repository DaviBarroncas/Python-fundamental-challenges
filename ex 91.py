from random import randint
from time import sleep
from operator import itemgetter
jogo= {"jogador 1": randint(1, 6),
      "jogador 2": randint(1, 6), 
      "jogador 3": randint(1, 6),
      "jogador 4": randint(1, 6),}
ranking=dict()
for i, k in jogo.items():
    print(f"{i} tirou {k}")
    sleep(1)
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("=-"*30)
for i, v in enumerate(ranking):
    print(f"{i+1}ª lugar:{v[0]} com {v[1]} ")
    sleep(1)