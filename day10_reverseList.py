l = eval(input("enter collection : "))
def reverseColl(l, s=0, e=len(l)-1):
    if s>e:
        return l
    l[s], l[e] = l[e], l[s]
    return reverseColl(l, s+1, e-1)

print(reverseColl(l))