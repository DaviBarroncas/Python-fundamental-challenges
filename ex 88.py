from random import randint
print("MEGA SENA: SORTEIO")
a=list()
jogos=list()
b=int(input("quantas vezes voce quer sortear? "))
c=1
while c <=b:
    c+=1
    d=0
    while True:
        e=randint(1, 60)
        if e not in a:
            a.append(e)
            d+=1
        if d>=6:
            break
    a.sort()
    jogos.append(a[:])
    a.clear()
for i, l in enumerate(jogos):
    print(f"jogo {i+1}: {l}")