# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:22:13 2023

@author: Daria
"""

from heys import int_to_bin
from diff_prob_F_table import V16, V4
import linecache
import time 
import ast


def check_if_in_list(el, list_of_tuples):
    for pair in list_of_tuples:
        if el == pair[0]:
            return True, pair[1]
    return False, None

def DifferentialSearch(alpha, prob_ = 0.01):
    Gamma_0 = [(alpha, 1)]
    for t in range(1, 7):
        Gamma_t = []
        for (beta_i, p_i) in Gamma_0:
            delta = linecache.getline('table_F.txt', int(beta_i, 2) + 1)
            delta = ast.literal_eval(delta)
            for (gamma_j, q_j) in delta:
                trig, prob = check_if_in_list(gamma_j, Gamma_t)
                if trig:
                    Gamma_t.remove((gamma_j, prob))
                    Gamma_t.append((gamma_j, prob + p_i*q_j))
                else:
                    Gamma_t.append((gamma_j, p_i*q_j))
        Gamma_t = [pair for pair in Gamma_t if pair[1] > prob_]
        Gamma_0 = Gamma_t
    return Gamma_t


if __name__ == '__main__':
    file = open('Gamma.txt', 'w')
    file.write('{')
    start = time.time()
    for v in V16[1:]:
        v_ = [int(v[j:j + 4], 2) for j in range(0, 16, 4)] 
        if v_.count(0) < 3:
            continue
        difs = DifferentialSearch(v)
        if difs == []:
            continue
        max_p = max([pair[1] for pair in difs])
        file.write("'" + v + "'" + ':')
        file.write(str([pair for pair in difs if pair[1] == max_p]) + ',')
        file.write('\n')
    file.write('}')
    file.close()
    print(time.time() - start)
