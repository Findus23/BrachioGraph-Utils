from io import TextIOWrapper
from typing import List, Tuple


def convert(file: TextIOWrapper) -> List[List[Tuple[float, float]]]:
    lines = []
    line = []
    firstlayer = True
    for textline in file:
        if not firstlayer:
            break
        textline = textline.split(";")[0]  # remove comments
        if textline == "\n" or textline == "":
            continue
        print(repr(textline))
        parts = textline.split()
        command = parts[0]

        if command not in ["G1"]:
            continue
        X = None
        Y = None
        E = False
        for attr in parts[1:]:
            print(attr)
            a = attr[0]
            num = float(attr[1:])
            if a == "X":
                X = num
            elif a == "Y":
                Y = num
            if a == "Z" and num > 0.3:
                firstlayer = False
            if a == "E":
                E = True
        if X and Y and E:
            line.append((X, Y))
        if command == "G1" and not E:
            if line:
                lines.append(line)
                line = []

    if line:
        lines.append(line)

    return lines
