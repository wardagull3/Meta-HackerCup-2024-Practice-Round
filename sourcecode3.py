# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nwq_oMiSrnfBrk-gGWJN3_Yjsa_uKITQ
"""

from collections import defaultdict
from math import gcd

def count_moves_to_collinear(ants):
    n = len(ants)

    if n <= 2:
        return 0  # All points are already collinear

    min_moves = float('inf')

    for i in range(n):
        slopes = defaultdict(int)
        for j in range(n):
            if i != j:
                dx = ants[j][0] - ants[i][0]
                dy = ants[j][1] - ants[i][1]

                # Reduce the slope to its simplest form
                if dx == 0:  # vertical line
                    slope = ('inf', 0)
                elif dy == 0:  # horizontal line
                    slope = (0, 'inf')
                else:
                    sign = -1 if (dx < 0) ^ (dy < 0) else 1
                    g = gcd(abs(dx), abs(dy))
                    slope = (sign * abs(dy) // g, abs(dx) // g)

                slopes[slope] += 1

        # The maximum number of collinear points with point i
        max_collinear = max(slopes.values(), default=0)
        min_moves = min(min_moves, n - 1 - max_collinear)  # Move the rest

    return min_moves

def main(input_file, output_file):
    with open(input_file, 'r') as infile:
        T = int(infile.readline().strip())  # Read number of test cases
        results = []

        for case_num in range(1, T + 1):
            N = int(infile.readline().strip())  # Read the number of ants
            ants = []

            for _ in range(N):
                x, y = map(int, infile.readline().strip().split())  # Read coordinates
                ants.append((x, y))

            moves_needed = count_moves_to_collinear(ants)  # Calculate moves
            results.append(f"Case #{case_num}: {moves_needed}")

    # Write results to output file
    with open(output_file, 'w') as outfile:
        for result in results:
            outfile.write(result + '\n')

# Example usage
if __name__ == "__main__":
    input_file = 'input3.txt'  # Input file name
    output_file = 'output3.txt'  # Output file name
    main(input_file, output_file)