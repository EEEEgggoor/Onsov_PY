s = str(input())
sp = list(map(int, s.split()))

def mins(sp):
    k=0
    fl = True
    while fl:
        if (0 not in sp):
            for i in range(len(sp)):
                sp[i]-=1
            k+=1
        else: fl = False
        if fl==False: break

    for i in range(len(sp)):
        if 0 in sp and sp.index(0)!=0 and sp.index(0)!=(len(sp)-1):
            k += sum(sp)
            return (k, sp)
        else:
            if len(set(sp))!=1:
                while 0 in sp: sp.pop(0)
                k += min(sp)
                return (k, sp)
            else: return (k, sp)

print(mins(sp))
