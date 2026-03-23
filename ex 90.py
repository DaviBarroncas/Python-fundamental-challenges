dados=dict()
dados["nome"]=input("Nome:")
dados["media"]=float(input(f"Média de {dados["nome"]}: "))
if dados["media"]<7:
    dados["situação"]="reprovado"
else:
    dados["sistuação"]="reprovado"

print(dados)
for i, l in dados.items():
    print(f"{i} = {l}")