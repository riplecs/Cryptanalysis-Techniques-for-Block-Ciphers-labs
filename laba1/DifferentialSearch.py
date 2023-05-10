# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:22:13 2023

@author: Daria
"""

from Heys import *

def differential_S(alpha, beta):
    return sum(int(S[i^alpha] == S[i]^beta) for i in range(2**4))/2**4

def diff_probs_table_S():
    table_S = np.zeros((2**4, 2**4))
    for i in range(2**4):
        for j in range(2**4):
            table_S[i][j] = differential_S(i, j)
    return table_S

def diff_probs_table_F():
    file = open('table_F.txt', 'w')
    table_S = diff_probs_table_S()
    for i in range(2**16):
        table_alpha_i = []
        for j in range(2**16):
            dp_F = 1
            for k in range(4):
                dp_F *= table_S[(i >> 4*k)&0xf][(j >> 4*k)&0xf]
            if dp_F != 0:
                table_alpha_i.append((bits_perm(j), dp_F))
        file.write(str(table_alpha_i) + '\n')
    file.close()
 
def DifferentialSearch(alpha, r = 6, prob = 0.001):
    Gamma_0 = {alpha: 1}
    for t in range(1, r):
        Gamma_t = {}
        print(Gamma_t)
        for beta_i in Gamma_0:
            delta = all_differentials[beta_i]
            for gamma_j in delta:
                if gamma_j in Gamma_t:
                    Gamma_t[gamma_j] += Gamma_0[beta_i]*delta[gamma_j]
                else:
                    Gamma_t[gamma_j] = Gamma_0[beta_i]*delta[gamma_j]
        Gamma_t = {k: v for k, v in Gamma_t.items() if v > prob}     
        Gamma_0 = Gamma_t
    return Gamma_t

if __name__ == '__main__':
    
    #diff_probs_table_F()
    
    file = open('table_F.txt', 'r')
    data = file.readlines()
    file.close()
    all_differentials = {i: dict(ast.literal_eval(data[i])) for i in range(2**16)}   
    
    for v in range(1, 2**16):
        if [v&0xf, (v >> 4)&0xf, (v >> 8)&0xf, (v >> 12)&0xf].count(0) < 3:
            continue
        difs = DifferentialSearch(v)
        if difs != {}:
            print('\t alpha = ', v)
            for b in difs:
                print(f'beta = {b}, DP({v}, {b}) = ', difs[b])
                
    '''
    for v in [6, 9, 1536, 24576, 36864, 45056]:
        print('\n\t alpha = ', v)
        for r in range(2, 7):
            difs = DifferentialSearch(v, r)
            if difs != {}:
                print('Round ',  r - 1)
                for b in difs:
                    print(f'beta = {b}, DP({v}, {b}) = ', difs[b])
                    if list(difs.keys()).index(b) > 3:
                        break
    '''
