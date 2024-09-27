
def movedisk(source,dest,n):
    print("move disk ",n," from source",source,"to destination",dest)
def TowerofHonoi(n,source,dest,aux):
    if n == 1:
        movedisk(source,dest,1)
        return
    TowerofHonoi(n-1,source,aux,dest)
    movedisk(source,dest,n)
    TowerofHonoi(n-1,aux,dest,source)
n=3
TowerofHonoi(n,"A","B","C")
