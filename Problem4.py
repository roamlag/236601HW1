'''
@author: galmaor
'''
from numpy.lib.scimath import logn
from random import randint
from time import clock
from booleanGaussianElimination import boolGaussianElimination

# All vectorsOfWeight of length n and weight at most k
def numsOfWeight(n, k):
    nums = []
    masks = [1 << j for j in range(n)]
    for num in xrange(1 << n):
        weight = 0
        for m in masks:
            if (num & m):
                weight += 1
        if weight <= k:
            nums.append(num)
    return nums

def hasHullRank(H, n, r):
    boolGaussianElimination(H, n, r)
    if 0 in H:
        return False 
    return True
    
def Vc_size(H, n, r, tests):
    legals = 0
#     for v in numsOfWeight(n, n - r):
    for v in tests:
        Hv = [j & (~v) for j in H]
        if (hasHullRank(Hv, n, r)):
            legals += 1
    return legals
    
def sum_rate(H, n, r, tests):
    return (logn(2, 2 * Vc_size(H, n, r, tests)) + r) / (n + 1)

def randomMatrix(n, r):
    H = []
    for _ in xrange(r):
        line = randint(0, 2 ** n - 1)
        H.append(line)
    return H

if __name__ == '__main__':
#     h = [116, 90, 105]
#     h1 = [77, 43, 23]
#     h2 = [60, 90, 105]
#     h6 = [56, 54, 35]
    patience = 10
    max_rate = 0
    best_matrix = []
    best_Vc = 0
    c = clock()

    n = 30
    r = n * 2 / 3
    theNumbers = numsOfWeight(n, n-r)
    for _ in xrange(patience):
        H = randomMatrix(n, r)
        rate = sum_rate(H,n,r, theNumbers)
        if rate > max_rate:
            max_rate = rate
            best_matrix = H
            print max_rate
            print H
        t = clock() - c
        print "time in seconds:",t
        c = clock()
    
    pass
