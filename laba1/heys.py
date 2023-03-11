# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:13:50 2023

@author: Daria
"""

import random 
import subprocess

S = ('F', '8', 'E', '9', '7', '2', '0', 'D', 'C', '6', '1', '5', 'B', '4', '3', 'A')
pi = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]


def int_to_bin(num, l):
    num = bin(num)[2:]
    while len(num) < l:
        num = '0' + num
    return num

S = [int_to_bin(int(s, 16), 4) for s in S]


def round_func(input_block, it, key):
    y = int_to_bin(int(input_block, 2)^key[it], 16)
    y = [y[j:j + 4] for j in range(0, 16, 4)]
    z = ''.join([S[int(y_i, 2)] for y_i in y])
    return ''.join([z[i] for i in pi])


def Heys(input_block, key):
    input_block = input_block[8:16] + input_block[0:8]
    for i in range(6):
        input_block = round_func(input_block, i, key)
    input_block = int_to_bin(int(input_block, 2)^key[-1], 2**4)
    return hex(int(input_block[8:16] + input_block[0:8], 2))[2:]


                    
if __name__ == '__main__':
    
    random.seed(100)

    KEY = bytes(random.randrange(0,255) for _ in range(14))
    key = open('key.bin', 'wb') 
    key.write(KEY)
    key.close()
    KEY = KEY.hex()
    KEY_hex = ''.join([KEY[i + 2:i + 4] + KEY[i:i + 2] for i in range(0, 28, 4)])
    KEY = [int(KEY_hex[i:i + 4], 16) for i in range(0, 28, 4)]
    print(round_func('0000010001001110', 1, KEY))
    #X = '7A1D'
    random.seed()
    X = hex(random.choice(range(2**16)))[2:]
    print('x = ', X)
    print('k = ', KEY_hex)
    print('E_k(x) = ', Heys(int_to_bin(int(X, 16), 16), KEY))
    print('Перевірка:')
    pt = open('x.bin', 'wb')
    pt.write(int(X, 16).to_bytes(2, 'big'))
    pt.close()
    subprocess.run('heys e 5 x.bin x_e.bin key.bin')
    cp = open("x_e.bin", "rb")
    c = cp.read()
    cp.close()
    print(c.hex())


