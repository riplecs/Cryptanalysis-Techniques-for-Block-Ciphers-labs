# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:51:10 2023

@author: Daria
"""

import time 
import numpy as np
from multiprocessing import Pool


from Heys import round_func
from LinearApproximationsSearch import dot
from AttackData import TEXTS, BEST_APPROXS


def M2(approx):
    alpha, beta = approx
    keys = np.zeros((2**16,))
    for k in range(2**16):
        u_k = 0
        for x, y in TEXTS:
            x1 = round_func(x, k)
            if dot(alpha, x1)^dot(beta, y) == 0:
                u_k += 1
            else:
                u_k -= 1
        keys[k] = abs(u_k)
    _, keys = zip(*sorted(zip(keys, range(2**16)), reverse = True))
    return keys[:100]


if __name__ == '__main__':
    
    print('Attack has started')
    
    start_time = time.time()
    keys = np.zeros((2**16,))
    with Pool() as pool:
        RESULTS = pool.map(M2, BEST_APPROXS)
    for mass in RESULTS:
        for k_i in mass:
            keys[k_i] += 1
    stat, keys = zip(*sorted(zip(keys, range(2**16)), reverse = True))
    
    print('Attack is finished succefully, time: %.2f s' % (time.time() - start_time))
    
    for i in range(10):
        print('k = ', keys[i], 'statistic = ', stat[i])
  
    
    
