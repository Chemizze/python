def notas(*n, sit=False):
    notas={}
    notas['tot']=len(n)
    notas['maior']=max(n)
    notas['menor']=min(n)
    notas['media']=sum(n)/len(n)
    if sit==True:
        if notas['media']>7.0:
            notas['situaçao']='BOA'
        elif notas['media']>=5.0:
            notas['situaçao']='RAZOAVEL'
        else:
            notas['situaçao']='Ruim'
    
    return notas


resp=notas(5.5, 9.5, 10, 6.5, sit=False)
print(resp)