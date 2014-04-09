'''
@author: galmaor
'''
def boolGaussianElimination(H,n,r):
    leaders = 0
    for col in range(n):
        exists = False
        mask = 1 << (n-1-col);
        for row in range(leaders,r):
            if (H[row] & mask):
                exists = True
                H[leaders],H[row]=H[row],H[leaders]
        if (exists):
            leaders += 1
            for row in range(leaders,r):
                if (H[row] & mask):
                    H[row] = H[row] ^ H[leaders-1]
    return H
