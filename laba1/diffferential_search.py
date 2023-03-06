# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:22:13 2023

@author: Daria
"""

file = open('table_F.txt', 'r')
table_F = file.readlines()

print(table_F[0])



def DifferentialSearch(alpha, prob = 0.25):
    Gamma = [[(alpha, 1)]]
    for t in range(1, 7):
        Gamma_t = []
        for (beta_i, p_i) in Gamma[t - 1]:
            for (gamma_i, q_i) in table_F[int(beta_i, 2)]:
                trig = True
                for pair in Gamma_t:
                    if gamma_i in pair:
                        pair[1] += p_i*q_i
                        trig = False
                if trig:
                    Gamma_t.append((gamma_i, p_i*q_i))
        for (gamma_i, p_i) in Gamma_t:
            if p_i <= prob:
                Gamma_t.remove((gamma_i, p_i))
        Gamma.append(Gamma_t)
    return Gamma[-1]