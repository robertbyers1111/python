#!/usr/bin/python3

def NativeZeros(nRows, nCols):
    return [range(nRows) for col in range(nCols)]

matrix = NativeZeros(4, 4)
print(matrix)
print(sum([sum(row) for row in matrix]))

