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


def M2(alpha, beta, texts):
    keys = np.zeros((2**16,))
    for k in range(2**16):
        u_k = 0
        for x, y in texts:
            x1 = round_func(x, k)
            if dot(alpha, x1)^dot(beta, y) == 0:
                u_k += 1
            else:
                u_k -= 1
        keys[k] = u_k
    _, keys = zip(*sorted(zip(keys, range(2**16)), reverse = True))
    return keys[:50]


def first_round_attack(approxs):
    keys = np.zeros((2**16,))
    for alpha, beta in approxs:
        print(alpha, beta)
        keys_ = M2(alpha, beta, TEXTS[:1000])
        for k in keys_:
            keys[k] += 1
    _, keys = zip(*sorted(zip(keys, range(2**16)), reverse = True))
    return keys[:10]


if __name__ == '__main__':
    
    print('Attack has started')
    
    start_time = time.time()
    
    with Pool(8) as pool:
        print(pool.map(first_round_attack, 
                       [BEST_APPROXS[i*50:i*50 + 50] for i in range(8)]))
        
    print('Attack is finished succefully, time: %.2f s' % (time.time() - start_time))
    