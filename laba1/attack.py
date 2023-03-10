# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:05:04 2023

@author: Daria
"""

import random
import subprocess

random.seed(100)
KEY = bytes(random.randrange(0,255) for _ in range(14))
with open('key.bin', 'wb') as f:
    f.write(KEY)
f.close()

def last_round_attack(alpha, beta, p):
    n = int(4//p)
    X, C = [], []
    for i in range(n):
        x = random.getrandbits(16)
        with open('x.bin', 'wb') as f:
            f.write(x.to_bytes(2, 'big'))
        f.close()
        subprocess.run('heys e 5 x.bin x_e.bin key.bin')
        with open("x_e.bin", "rb") as f:
            byte = f.read()
        c = int(byte.hex(), 16)
        x_ = x^alpha
        with open('x.bin', 'wb') as f:
            f.write(x_.to_bytes(2, 'big'))
        f.close()
        subprocess.run('heys e 5 x.bin x_e.bin key.bin')
        with open("x_e.bin", "rb") as f:
            byte = f.read()
        c_ = int(byte.hex(), 16)
        X.append((x, x_))
        C.append((c, c_))
    K = []
    for k in range(2**16):
        count = 0
        for (c, c_) in C:
            y, y_ = c^k, c_^k
            if y_ == y^beta:
                count += 1
        K.append(count)
    print(K)
    return K.index(max(K))

print(last_round_attack(int('0000011000000000', 2), int('0000100000000000', 2), 0.067535400390625))