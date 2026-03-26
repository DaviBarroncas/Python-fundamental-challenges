from time import sleep
def maior(*num):
    cont=maior=0
    print("-="*30)
    print("\n analisando os valores passados...")
    for valor in num:
        print(f"{valor}", end="")
        sleep(0.3)
        if cont==0:
          maior=valor
        else:
           if valor > maior:
              cont+=1
    print(f"\nforam ubformados {cont} valores ao todo")
    print(f"\no maior valor foi {maior}")


maior(2, 9, 4, 5, 7, 9)
maior(4,7, 8)
maior(1, 2)
maior(6)
maior()