# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sF0_lzjObXKvfQyXTlKB_27xzs37YBSc
"""

def calculate_increase(N, P):
    P_prime = 100 * (P / 100) ** ((N - 1) / N)
    return P_prime - P

with open('input2.txt', 'r') as infile, open('output2.txt', 'w') as outfile:
    T = int(infile.readline().strip())
    results = []
    for t in range(1, T + 1):
        N, P = map(int, infile.readline().strip().split())
        increase = calculate_increase(N, P)
        results.append(f"Case #{t}: {increase:.15f}")

    outfile.write("\n".join(results) + "\n")