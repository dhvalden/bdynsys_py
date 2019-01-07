import numpy as np
from polyfitreg import polyfitreg

def combs(v, k):
    n = len(v)
    if n == k:
        P = np.array(v, 1, n) # not the real format
    elif k == 1:
        P = np.array(v, n, 1)
    elif k == n-1:
        P = np.array(np.repeat(v, each = n-1), n, n-1) # not the real format
        if k < n and k > 1:
            for i in range(1:(n - k + 1)):
                Q = combs(v[(i + 1):n+1] k - 1) # not the real format
                j = Q.shape[0]
                P = np.concatenate((P, np.concatenate((np.repeat(v[i], j), Q),
                                                      axis = 1), axis = 0)) #check here!
    
def bestfitmod(paramnr, xv, yv, ch):
    nmodelterms = paramnr
    nterms = 17
    
    SEtest = np.full((nterms, int(choose(nterms, nmodelterms))), 100, order = "F")
    
    ridx = np.arange(len(xv))
    np.random.shuffle(ridx)

    xtrain = xv[ridx]
    ytrain = yv[ridx]
    chtrain = ch[ridx]
    print(chtrain)

    for i in range(1, nmodelterms):
        M <- combs(1:nterms, i)
        for j in range(1, M.rows()):
            tmp = polyfitreg(xtrain, ytrain, chtrain, M[j, ])
            B = tmp[[1]]
            err = tmp[[2]]
            SEtest[i, j] = err
    return SEtest

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
ch = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


bestfitmod(6, x, y, ch)
