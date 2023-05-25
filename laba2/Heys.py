# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:13:50 2023

@author: Daria
"""

import random 
import subprocess
import linecache
import ast


S = [0xf, 8, 0xe, 9, 7, 2, 0, 0xd, 0xc, 6, 1, 5, 0xb, 4, 3, 0xa]
pi = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]


random.seed(100)


def bits_perm(x):
    result = 0
    for i, j in enumerate(pi):
        if x&(1 << j): 
            result |= (1 << i)
    return result

def round_func(x, key):
    x ^= key
    y0, y1, y2, y3 = x&0xf, (x >> 4)&0xf, (x >> 8)&0xf, (x >> 12)&0xf
    z0, z1, z2, z3 = S[y0], S[y1], S[y2], S[y3]
    z = (z3 << 12) + (z2 << 8) + (z1 << 4) + z0
    return bits_perm(z)

def Heys(x, key):
    for i in range(6):
        x = round_func(x, key[i])
    x ^= key[-1]
    return x
                    
if __name__ == '__main__':
    
    X = 0x7a1d

    KEY = bytes(random.randrange(0, 255) for _ in range(14))
    with open('key.bin', 'wb') as f:
        f.write(KEY)
    KEY = KEY.hex()
    KEY = [KEY[i + 2:i + 4] + KEY[i:i + 2] for i in range(0, 28, 4)]
    print('x = ', hex(X)[2:])
    print('k = ', KEY)
    KEY = [int(k, 16) for k in KEY]
    X_e = Heys(X, KEY)
    print('E_k(x) = ', hex(X_e)[2:])
    print('Перевірка:')
    with open('x.bin', 'wb') as f:
        f.write(X.to_bytes(2, 'little'))
    subprocess.run('heys e 5 x.bin x_e.bin key.bin')
    with open('x_e.bin', 'rb') as f:
        x_e = f.read()
    print('E_k(x) = ', hex(int.from_bytes(x_e, 'little'))[2:])
