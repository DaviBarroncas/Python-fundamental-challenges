print("BOLETIM COM LISTAS COMPOSTAS")
alunos=list()
while True:
    a=input("nome: ")
    b=int(input("nota 1: "))
    c=int(input("nota 2:"))
    media= (b+c)/2
    alunos.append([a, [b, c], media])
    d=input("Quer continuar[S/N?]? ".upper())
    if d in "Nn":
        break
for i, l in enumerate(alunos):
    print(f"{i:<4}{a[0]:<10}{l[2]:>8.1f}")

