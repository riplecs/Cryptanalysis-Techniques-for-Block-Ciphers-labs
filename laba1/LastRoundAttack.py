# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 08:05:14 2023

@author: Daria
"""

from Heys import *

def collect_ct(alpha, n = 4000):
    cipher_texts = []
    for x in range(n):
        with open('x.bin', 'wb') as f:
            f.write(x.to_bytes(2, 'little'))
        subprocess.run('heys e 4 x.bin x_e.bin')
        with open('x_e.bin', 'rb') as f:
            c = int.from_bytes(f.read(), 'little')
        x ^= alpha
        with open('x.bin', 'wb') as f:
            f.write(x.to_bytes(2, 'little'))
        subprocess.run('heys e 4 x.bin x_e.bin')
        with open('x_e.bin', 'rb') as f:
            c_ = int.from_bytes(f.read(), 'little')
        cipher_texts.append((c, c_))
    return cipher_texts
    

def last_round_attack(cipher_texts, beta):
    Keys = []
    for k in range(1, 2**16):
        count = 0
        for (c, c_) in cipher_texts:
            y = inv_round_func(c, k)
            y_ = inv_round_func(c_, k)
            if y_^y in beta:
                count += 1
        Keys.append(count)
    return Keys.index(max(Keys)) + 1

    
if __name__ == '__main__':
    
    TEXTS = collect_ct(24576)
    print('Last round key: ', hex(last_round_attack(TEXTS, [1088, 16452, 17476, 1632]))[2:])
    
    #TEXTS = collect_ct(6)
    #print('Last round key: ', hex(last_round_attack(TEXTS, [544, 8226, 8738]))[2:])
