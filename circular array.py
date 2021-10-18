
def circularArrayRotation(a, k, queries):
    t=[]
    for i in range(k):
        x=a.pop()
        a.insert(0,x)
    for i in queries:                         """hackerrank"""
        t.append(a[i])
    return t
