def jogador(n, g):
    if g not in "0123456789" or g in "":
        g=0 
    print(f"o jogador {n} fez {g} gols")

nome= input("Nome: ")
gols= input("Gols: ")
jogador(nome, gols)