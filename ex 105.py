def notas(*n, sit=False):
    
    
    y=dict()
    y["total"]=len(n)
    y["media"]=sum(n)/len(n)
    y["maior"]=max(n)
    y["menor"]=min(n)
    if sit:
        if y["media"]>7:
            y["situação"]= "APROVADO(A)"
        else:
            y["situação"]= "REPROVADO(A)"
    return y





resp=notas(5.5,2.5, 1.5, sit=True)
print(resp)