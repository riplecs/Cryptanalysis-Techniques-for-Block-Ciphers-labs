# -*- coding: utf-8 -*-
"""
Created on Wed May 24 11:18:04 2023

@author: Daria
"""
import ast

with open('TEXTS.txt', 'r') as f:
    data = f.readlines()
TEXTS = ast.literal_eval(data[0])


with open('BEST_APPROXS.txt', 'r') as f:
    data = f.readlines()
BEST_APPROXS = [ast.literal_eval(d) for d in data]

