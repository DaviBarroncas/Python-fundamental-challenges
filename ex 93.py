jogo=dict()
partidas = list()
jogo["nome"]=input(" nome do jogador? ")
tot=int(input("Quantos jogas ele jogou? "))
for q in range (1, tot+1):
    partidas.append( int(input(f"quantos gols o {jogo["nome"]} fez na partida {q}? ")))
jogo["gol"]= partidas[:]
print("-="*30)
print(jogo)
print("-="*30)
jogo["total"]= sum(partidas)
for k, l in jogo.items():
    print(f"O Campo {k} tem o valor {l}")
print("-="*30)
print(f"o jogador {jogo["nome"]} jogou {len(jogo["gol"])} jogos")
for i, v in enumerate(jogo["gol"]):
    print(f"      =>       NA partida {i}, fez {v} gols")
    print(f"foi um total de {jogo["total"]} gols")