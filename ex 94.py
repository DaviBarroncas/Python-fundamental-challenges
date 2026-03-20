dados=dict()
id=list()
soma=media=0
while True:
    dados.clear()
    dados["nome"]= input("nome: ")
    while True:
        dados["sexo"]= input("sexo[M/F]: ").upper()
        if dados["sexo"] in "MF":
            break
        print("ERRO: responda apenas com M ou F")
    dados["idade"]= int(input("Idade: "))
    soma+=dados["idade"]
    id.append(dados.copy())
    while True:
        c=input("Quer continuar[S/N]? ").upper()
        if c in "SN":
            break
        print("S ou N")
    if c in "Nn":
        break  
    
media=soma/len(id)
print(f"A) ao todo temos {len(id)} cadastrados")
print(f"B) a media de idade é de {media:5.2f} anos")
print(f"C) as mulheres cadastradas foram")
for p in id:
    if p["sexo"] in "F":
        print(f"{p["nome"]}", end= " ")
print()