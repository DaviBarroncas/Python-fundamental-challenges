jogador=dict()
partidas=list()
time=list()
while True:
    jogador.clear()
    jogador["nome"]= input("Nome do jogador: ")
    tot= int(input(f"quantas partidas {jogador["nome"]} jogou ?"))
    partidas.clear()
    for l in range(0, tot ):
        partidas.append(int(input(f"Quantas gols fez no jogo {l+1}?")))
    jogador["gols"]=partidas[:]
    jogador["total"]=sum(partidas)
    time.append(jogador.copy())
    c=input("deseja continuar[S/N]? ").upper()
    if c in "Nn":
        break
print("-="*30)
print("cod", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-="*30)
for k,v  in enumerate(time):
    print(f"{k:>3}", end= '')
    for d in v.values():
       print(f"{str(d):<15}", end= "")
    print()
print("-="*30)
while True:
    busca= int(input("Mostrar dados de qual jogador? "))
    if busca==999:
        break
    if busca>= len(time):
        print("ERRO. Não existe jogador com esse código")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR -- {time[busca]["nome"]}")
        for i, g in enumerate(time[busca]["gols"]):
            print(f"no jogo {i+1} fez {g} gols")
print(f"o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas)")
for i, v in enumerate(jogador["gols"]):
    print(f"   =>     na partida {i}, fez {v} gols")
print(f"foi um total de {jogador["total"]} gols")
print(partidas)
print(jogador)