# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:13:50 2023

@author: Daria
"""

import random 

from diff_prob_F_table import int_to_bin, S, pi

random.seed(100)


#KEY = [random.getrandbits(16) for i in range(7)]
KEY = bytes(random.randrange(0, 255) for _ in range(14)).hex()
KEY_hex = ''.join([KEY[i + 2:i + 4] + KEY[i:i + 2] for i in range(0, 28, 4)])
KEY = [int(KEY_hex[i:i + 4], 16) for i in range(0, 28, 4)]


def round_func(input_block, it):
    y = int_to_bin(int(input_block, 2)^KEY[it], 16)
    y = [y[j:j + 4] for j in range(0, 16, 4)]
    z = ''.join([S[int(y_i, 2)] for y_i in y])
    return ''.join([z[i] for i in pi])


def Heys(input_block):
    input_block = input_block[8:16] + input_block[0:8]
    for i in range(6):
        input_block = round_func(input_block, i)
    input_block = int_to_bin(int(input_block, 2)^KEY[-1], 2**4)
    return hex(int(input_block[8:16] + input_block[0:8], 2))[2:]


                    
if __name__ == '__main__':
    
    X = '7A1D'
    
    print('x = ', X.lower())
    print('k = ', KEY_hex)
    print('E_k(x) = ', Heys(int_to_bin(int(X, 16), 16)))


