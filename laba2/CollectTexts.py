# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:23:25 2023

@author: Daria
"""

from subprocess import Popen, PIPE 

def collect_ct(n = 10000):
    texts = []
    for x in range(n):
        with open('x.bin', 'wb') as f:
            f.write(x.to_bytes(2, 'little'))
        Popen('heys e 4 x.bin x_e.bin', stdin = PIPE).communicate('\n'.encode())
        with open('x_e.bin', 'rb') as f:
            c = int.from_bytes(f.read(), 'little')
        texts.append((x, c))
    return texts

if __name__ == '__main__':
    
    TEXTS = collect_ct()
    with open('TEXTS.txt', 'w') as f:
        f.write(str(TEXTS))
