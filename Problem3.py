'''
@author: galmaor
'''

EPSILON = 1e-10

# Problem 3
# number of legal sequences of length t with q symbols
def N(t, q):
    if (q == 0): return 0
    if (t == 1): return q
    return sum([N(t - 1, qq) for qq in range(q + 1) ])

# probability to succeed in writing t times
def P(t, q):
    return float(N(t, q)) / q ** t

def E(q):
    theSum = 0
    t = 1
    p = P(t, q)
    while (p > EPSILON):
        theSum += p
        t += 1
        p = P(t, q)
    return theSum

if __name__ == '__main__':
    print E(7)
    print 2*E(4)

    
    pass
