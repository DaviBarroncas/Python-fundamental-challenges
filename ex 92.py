from datetime import datetime
dados= dict()
dados["nome"]=input("nome: ")
nasc= int(input("Ano de nascimento: "))
dados["ctps"]=int(input("Sua carteira de trabalho(digite 0 se não tem): "))
if dados["ctps"]==0:
    dados["ctps"]="Sem experência"
else:
    dados["contratação"]= int(input("ano de contratação: "))
    dados["salário"]= int(input("seu piso salarial: R$"))
    dados["aposentadoria "]= ((dados["contratação"]+35)-datetime.now().year)
print(dados)
for k, v in dados.items():
    print(f"    -    {k} tem o valor {v}")