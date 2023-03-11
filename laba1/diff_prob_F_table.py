# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 08:05:14 2023

@author: Daria
"""

import time
from heys import int_to_bin, S, pi


V4 = [int_to_bin(i, 4) for i in range(2**4)]
V16 = [int_to_bin(i, 16) for i in range(2**16)]
V16_pi = [''.join(v[i] for i in pi) for v in V16]
V16_split = [[v[j:j + 4] for j in range(0, 16, 4)] for v in V16]
V16_split_pi = [[v[j:j + 4] for j in range(0, 16, 4)] for v in V16_pi]


def differential_S(alpha, beta):
    return sum(int(int(S[i^alpha], 2) == int(S[i], 2)^beta) 
                                                    for i in range(2**4))/2**4

def diff_probs_table_S():
    table_S = {}
    for i in range(2**4):
        table_alpha_i = []
        for j in range(2**4):
            prob = differential_S(i, j)
            table_alpha_i.append((V4[j], prob))
        table_S[V4[i]] = table_alpha_i
    return table_S


def diff_probs_table_F():
    file = open('table_F.txt', 'w')
    table_S = diff_probs_table_S()
    for alpha in V16_split:
        table_alpha_i = []
        for beta in V16_split:
            beta_ = V16_split_pi[V16_split.index(beta)]
            dp_F = 1
            for k in range(4):
                dp_F *= table_S[alpha[k]][V4.index(beta_[k])][1]
            if dp_F != 0:
                table_alpha_i.append((''.join(beta), dp_F))
        file.write(str(table_alpha_i) + '\n')
    file.close()
    
    
if __name__ == '__main__':
    start = time.time()
    diff_probs_table_F()
    end = time.time()
    print(end - start) 
