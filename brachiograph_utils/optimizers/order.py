import math
from typing import Tuple


def closest(point, paths) -> Tuple[list, bool]:
    next = None
    dist = float("Inf")
    rev = None
    for p in paths:
        endpoint = p[-1]
        start = p[0]
        # print(endpoint[0])
        distance = math.sqrt((point[0] - start[0]) ** 2 + (point[1] - start[1]) ** 2)
        revdistance = math.sqrt((point[0] - endpoint[0]) ** 2 + (point[1] - endpoint[1]) ** 2)
        if distance < dist:
            next = p
            dist = distance
            rev = False
        if revdistance < dist:
            next = p
            dist = distance
            rev = True
    return next, rev


def optimize(data):
    l = data[0]
    data.remove(l)
    output = [l]
    while data:
        endpoint = l[-1]
        next, rev = closest(endpoint, [p for p in data if p != endpoint])
        data.remove(next)
        if rev:
            next = next[::-1]
        output.append(next)
        l = next
    return output
