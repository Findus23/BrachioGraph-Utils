"""
inspired by https://nbviewer.jupyter.org/gist/martinfiers/e8f3efce89e099653d87fb47a8e10b0e
see also https://gist.github.com/martinfiers/e8f3efce89e099653d87fb47a8e10b0e
"""

from math import sqrt

import numpy as np
from numba import njit


@njit
def norm(start, end):
    # return linalg.norm(start - end)
    return sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)


@njit
def maxnorm(start, end):
    return max([start[0] - end[0], start[1] - end[1]])


@njit
def shuffle_line(lines):
    lines = lines[:]
    i, j = np.random.choice(np.arange(1, len(lines) - 1), 2, replace=False)
    lines[i], lines[j] = lines[j], lines[i]
    return lines


@njit
def swap_neighbors(lines):
    lines = lines[:]
    i = np.random.randint(1, len(lines) - 3)
    lines[i], lines[i + 1] = lines[i + 1], lines[i]
    return lines


@njit
def flip_line(lines):
    lines = lines[:]
    for _ in range(np.random.randint(1, 20)):
        i = np.random.choice(np.random.randint(1, len(lines) - 1))
        # lines[i] = np.fliplr(lines[i])
        # lines[i]=lines[i][::-1]
        new_array = np.copy(lines[i])
        l = len(new_array)
        for j in range(l):
            new_array[j] = lines[i][l - j - 1]
        lines[i] = new_array
    return lines


@njit
def total_length(lines):
    total = 0
    i = 0
    while i < len(lines) - 1:
        start = lines[i][-1]
        end = lines[i + 1][0]
        n = norm(start, end)
        total += n
        i += 1
    return total


# npdata.append(np.array([[300.0, 0.0]]))

@njit
def run(npdata, iterations):
    current_length = total_length(npdata)
    # new_list = shuffle_line(npdata)
    print(current_length)

    i = 0
    while i < iterations:
        r = np.random.rand()
        if r > 0.5:
            new_list = flip_line(npdata)
        elif r < 0.3:
            new_list = swap_neighbors(npdata)
        else:
            new_list = shuffle_line(npdata)
        new_length = total_length(new_list)
        if new_length < current_length:
            npdata = new_list
            current_length = new_length
            print(new_length, current_length)
        i += 1
        if i % 10000 == 0:
            print(i)
    return npdata


def optimize(data, iterations):
    npdata = []
    for line in data:
        npdata.append(np.array(line))

    a = run(npdata, iterations)
    print(total_length(a))
    data = [l.tolist() for l in a]

    return data
