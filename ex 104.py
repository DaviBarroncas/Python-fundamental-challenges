def leiaint(num):
    ok= False
    valor=0
    while True:
        n=str(input(num))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print("\033[0;31mERRO: Digite um numero inteiro válido.\033[m")
        if ok:
            break   
    return valor



n=leiaint("digite um número: ")
print(f"voce acabou de digitar o numero {n}")