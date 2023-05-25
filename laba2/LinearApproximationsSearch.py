# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:27:16 2023

@author: Daria
"""

import numpy as np
import ast
import pandas as pd

from Heys import bits_perm, S


def dot(x, y):
    return bin(x&y).count('1')%2


def count_matches(alpha, beta):
    return sum(int(dot(alpha, i) - dot(beta, S[i]) == 0) for i in range(2**4))


def linear_approximations_S():
    table_S = np.zeros((2**4, 2**4))
    for i in range(2**4):
        for j in range(2**4):
            table_S[i][j] = count_matches(i, j) - 8
    return table_S


def linear_potential(alpha, beta):
    return (sum((-1)**(dot(alpha, x)^dot(beta, S[x])) for x in range(2**4))/2**4)**2


def linear_potentials_S():
    table_S = np.zeros((2**4, 2**4))
    for i in range(2**4):
        for j in range(2**4):
            table_S[i][j] = linear_potential(i, j)
    return table_S


def linear_approxs_table_F():
    file = open('table_F.txt', 'w')
    table_S = linear_potentials_S()
    for i in range(2**16):
        table_alpha_i = []
        for j in range(2**16):
            dp_F = 1
            for k in range(4):
                dp_F *= table_S[(i >> 4*k)&0xf][(j >> 4*k)&0xf]
            if dp_F != 0:
                table_alpha_i.append((bits_perm(j), dp_F))
        if table_alpha_i == []:
            file.write(str(table_alpha_i) + '\n')
    file.close()
    
    
def LinearApproximationsSearch(alpha, r = 6, lim = 0.0001):
    Gamma_0 = {alpha: 1}
    for t in range(1, r):
        Gamma_t = {}
        for beta_i in Gamma_0:
            delta = ALL_APPROX[beta_i]
            for gamma_j in delta:
                if gamma_j in Gamma_t:
                    Gamma_t[gamma_j] += Gamma_0[beta_i]*delta[gamma_j]
                else:
                    Gamma_t[gamma_j] = Gamma_0[beta_i]*delta[gamma_j]
        Gamma_t = {k: v for k, v in Gamma_t.items() if v > lim}     
        Gamma_0 = Gamma_t
    return Gamma_t


def BestApproximations():
    best_app = []
    for v in range(1, 2**16):
        if [v&0xf, (v >> 4)&0xf, (v >> 8)&0xf, (v >> 12)&0xf].count(0) < 3:
            continue
        approxs = LinearApproximationsSearch(v)
        if approxs != {}:
            print('\t alpha = ', v)
            for b in approxs:
                print(f'beta = {b}, ELP({v}, {b}) = ', approxs[b])
                best_app.append((v, b))
    return best_app


if __name__ == '__main__':
    
    #print(pd.DataFrame(linear_approximations_S()))
    #print(pd.DataFrame(linear_potentials_table_S()).round(4))
    
    #potentials = linear_approxs_table_F()
    
    file = open('table_F.txt', 'r')
    data = file.readlines()
    file.close()
    ALL_APPROX = {i: dict(ast.literal_eval(data[i])) for i in range(2**16)}
    
    best_approximations = BestApproximations()    
    with open('BEST_APPROXS.txt', 'w') as f:
        f.write(str(best_approximations))