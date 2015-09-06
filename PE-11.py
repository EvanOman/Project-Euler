import numpy as np
import csv

def getHorizontalChunks(grid, chunkLength):
    n = chunkLength
    return [row[i:i+n] for row in grid for i in range(len(row) - (n-1))]

def getVerticalChunks(grid, chunkLength):
    return getHorizontalChunks(grid.T, chunkLength)

def getForwardDiagChunks(grid, chunkLength):
    diags = []
    leng = grid.shape[1]
    for i in range(grid):
        diag.append([grid[i - j, -(j+1)] for j in range(i+1)])

    for i,_ in enumerate(grid[-1,:]):
       # TODODODODOD 

def getBackwardDiagChunks(grid, chunkLength):
    return -1

def getGrid():
    r = csv.reader(open("PE-11-Data"), delimiter="s")
    strRows = [row[0] for row in r]
    grid = np.array([])
    for strRow in strRows:
        grid = np.append(grid, [int(x) for x in strRow.split()])
    grid.shape = (20,20)
    return grid


# Get the individual numbers from the grid
grid = getGrid()

