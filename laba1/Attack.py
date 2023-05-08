# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 08:05:14 2023

@author: Daria
"""

from Heys import *

def collect_ct(alpha, n = 1000):
    cipher_texts = []
    for x in range(n):
        with open('x.bin', 'wb') as f:
            f.write(x.to_bytes(2, 'little'))
        subprocess.run('heys e 5 x.bin x_e.bin key.bin')
        with open('x_e.bin', 'rb') as f:
            c = int.from_bytes(f.read(), 'little')
        x ^= alpha
        with open('x.bin', 'wb') as f:
            f.write(x.to_bytes(2, 'little'))
        subprocess.run('heys e 5 x.bin x_e.bin key.bin')
        with open('x_e.bin', 'rb') as f:
            c_ = int.from_bytes(f.read(), 'little')
        cipher_texts.append((c, c_))
    return cipher_texts
    

def last_round_attack(cipher_texts, betas):
    Keys = []
    for k in range(1, 2**16):
        count = 0
        for (c, c_) in cipher_texts:
            y = inv_round_func(c, k)
            y_ = inv_round_func(c_, k)
            if y_^y in betas:
                count += 1
        Keys.append(count)
    return Keys.index(max(Keys)) + 1

    
if __name__ == '__main__':
    
    TEXTS = collect_ct(1024)
    beta = [273, 4369, 2184, 17]
    
    print('Last round key: ', hex(last_round_attack(TEXTS, beta) + 1)[2:])
    
    TEXTS = collect_ct(3072)
    beta = [273, 4368, 4369, 1, 17]
    
    print('Last round key: ', hex(last_round_attack(TEXTS, beta))[2:])
