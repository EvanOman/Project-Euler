import numpy as np
import csv

def getHorizontalChunks(grid, chunkLength):
    n = chunkLength
    return [row[i:i+n] for row in grid for i in range(len(row) - (n-1))]

def getVerticalChunks(grid, chunkLength):
    return getHorizontalChunks(grid.T, chunkLength)

def getForwardDiagChunks(grid, chunkLength):
    diags = []

    # Gathers the upper triangle forward diagonals
    diags = getUpperForwardDiags(grid)

    # Gathering the lower triangle forward diagonals is the same on the transpose
    diags += getUpperForwardDiags(grid.T)

    return getChunkFromDiags(diags, chunkLength)

def getUpperForwardDiags(grid):
    diags = []
    leng = grid.shape[1]

    # Gathers the upper triangle forward diagonals
    for i in range(leng):
        diags.append([(grid[i - j, -(j+1)], i-j,leng-(j+1)) for j in range(i+1)])

    return diags

def getChunksFromDiags(diags, chunkLength):
    chunks = []
    n = chunkLength
    for i,_ in enumerate(diags):
        diag = diags[i]
        if len(diag) >= chunkLength:
            chunks += [diag[i:i+n] for i in range(len(diag) - (n-1))]
    return chunks

def getBackwardDiagChunks(grid, chunkLength):
    # The back ward diagonals are simply the forward diagonals of the rotated matrix
    return getForwardDiagChunks(np.rot90(grid), chunkLength)

def getAllChunks(grid, chunkLength):
    chunks = []
    chunks += getHorizontalChunks(grid, chunkLength)
    chunks += getVerticalChunks(grid, chunkLength)
    chunks += getForwardDiagChunks(grid, chunkLength)
    chunks += getBackwardDiagChunks(grid, chunkLength)
    return chunks

def getGrid():
    r = csv.reader(open("PE-11-Data"), delimiter="s")
    strRows = [row[0] for row in r]
    grid = np.array([])
    for strRow in strRows:
        grid = np.append(grid, [int(x) for x in strRow.split()])
    grid.shape = (20,20)
    return grid

# A few quick utility function
def mult(a,b): return a*b
def prod(ls): return reduce(mult, ls, 1)

# Get the individual numbers from the grid
grid = getGrid()

# Want to get all of the chunks of length 4
chunks = getAllChunks(grid, 4)

# Now we want to sort by the product of each chunk



