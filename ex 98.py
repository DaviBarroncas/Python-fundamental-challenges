from time import sleep
def contador(i, f, p):
    print("-="*20)
    print(f"\n contagem de {i} até {f} de {p} em {p}")
    sleep(2.5)
    if p<0:
        p*=-1
    if p==0:
        p=1
    if i<f:
        cont=i
        while cont <=f:
            print(f" {cont} ", end="", flush=True)
            sleep(0.5)
            cont+=p
    else: 
        cont= i
        while cont >= f:
            print(f" {cont} ", end="", flush=True)
            sleep(0.5)
            cont-=p
    

contador(1, 10, 1)
contador(10, 0 , 2)

print("AGORA É A SUA VEZ DE PERSONALIZAR A CONTAGEM")
ini=int(input("INICIO: "))
fim=int(input("FIM: "   ))
pas=int(input("passo: " ))
contador(ini, fim, pas)
