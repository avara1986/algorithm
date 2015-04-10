#!/usr/bin/env python
from itertools import permutations

n = 8
cols = range(n)
sols = []
for vec in permutations(cols):
    if n == len(set(vec[i] + i for i in cols)) and n == len(set(vec[i] - i for i in cols)):
        sols.append(vec)

for sol in sols:
    print sol