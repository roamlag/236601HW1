'''
@author: galmaor
'''

from Problem4 import numsOfWeight
from random import randrange
from numpy.lib.scimath import logn


def numsOfWeightMoreThan(n,k):
    leights = numsOfWeight(n, k)
    return [i for i in range(1 << n) if (i not in leights)]

F = {}

# n=5
# k=2

n=10
k=3

leights = numsOfWeight(n, k)
heavies = numsOfWeightMoreThan(n, k)
    
def isNeighbor(l,h):
    return l&h==l

def neighbors(j):
    return [k for k in heavies if isNeighbor(j, k)]

def neighborsNotAssigned(j):
    neighs = neighbors(j)
    keys = F.keys()
    return [k for k in neighs if (k not in keys)]

def chooseAtRandom (thelist):
    idx = randrange(0,len(thelist))
    return thelist[idx]

def createRandomMapping():
    for i in range(1,1<<n):
        for l in leights:
            keys = F.keys()
            neighs = neighbors(l)
            already = [F[j] for j in keys if (j in neighs)]
            if i in already:
                continue
            possibles = neighborsNotAssigned(l)
            if len(possibles) == 0:
                return i-1
            h = chooseAtRandom(possibles)
            F[h]=i

if __name__ == '__main__':
    M_2 = createRandomMapping()
    print M_2,F
    print "sum-rate:",(logn(2, len(leights)) + logn(2, M_2)) / n

#     print "$S_L$:",leights,"\\\\"
#     print "$S_R$:",heavies,"\\\\"
#     print "\\\\"
#     for l in leights:
#         print "neighbors of",l,"are:",neighbors(l),"\\\\"
    
    
    pass