from math import factorial

def num(y, show= False):
    f=1
    for c in range(y,0,-1):
        if show:
            print(c, end="")
            if c>1:
                print(" x ", end="")
            else: 
                print("=", end="")
        f*=c
    return f



print(num(int(input("digite um valor: ")), show=True))