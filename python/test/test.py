import sys
import pprint

sys.path.append("../src")

import utils
import wrap
import solve

def loadMatrix(file_A, file_b):
    with open(file_A) as file_object:
        lines = file_object.readlines()

    matrix = []
    for line in lines:
        if line == "":
            break
        line = line.split()
        line = [float(x) for x in line]
        matrix.append(line)

    with open(file_b) as file_object:
        lines = file_object.readlines()

    b = []
    for num in lines:
        if num == "":
            break
        num = float(num)
        b.append(num)

    return matrix, b


def main():
    if len(sys.argv) > 2:
        matrix, b = loadMatrix(sys.argv[1], sys.argv[2])
    else:
        matrix = [
            [11, 12, 0, 14, 0, 0],
            [-12, 22, 23, 0, 0, 0],
            [0, -23, 33, 0, 0, 0],
            [-14, 0, 0, 44, 0, 46],
            [0, 0, 0, 0, 55, 0],
            [0, 0, 0, -46, 0, 66]
        ]
        b = [91, 101, 53, 438, 275, 212]

    n = len(matrix)

    regen = []
    for i in range(n):
        regen.append([0] * n)

    triL = wrap.generateEnvelope(matrix, True)
    triU = wrap.generateEnvelope(matrix, False)

    wrap.unwrapEnvelope(triL, regen, True)
    wrap.unwrapEnvelope(triU, regen, False)

    i = 0
    j = 0
    while i < n:
        if regen[i][j] != matrix[i][j]:
            print(f"{matrix[i][j]} != {regen[i][j]}")

        j = j + 1
        if j == n:
            i = i + 1
            j = 0

    solve.luDecomposition(triL, triU)

    y = solve.solveForwardSubstitution(triL, b)
    x = solve.solveBackwardSubstitution(triU, y)

    print(x)

if __name__ == "__main__":
    main()