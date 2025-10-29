"""You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth. We will call a cell of the map a cavity if and only if this cell
is not on the border of the map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side, or edge. Find all the cavities on the
map and replace their depths with the uppercase character X. Example.

The grid is rearranged for clarity:
989
191
111

Return:
989
1X1
111

The center cell was deeper than those on its edges: [8,1,1,1]. The deep cells in the top two corners do not share an edge with the center cell, and none of the border cells is eligible.

Function Description

Complete the cavity_map function in the editor below.
cavity_map has the following parameter(s):
string grid[n]: each string represents a row of the grid
Returns
string{n}: the modified grid
"""


def get_adjacent_cells(grid: list[str], i: int, j: int) -> list[str]:
    adjacent_cells = []
    n = len(grid)
    if i > 0:
        adjacent_cells.append(grid[i - 1][j])
    if i < n - 1:
        adjacent_cells.append(grid[i + 1][j])
    if j > 0:
        adjacent_cells.append(grid[i][j - 1])
    if j < n - 1:
        adjacent_cells.append(grid[i][j + 1])
    return adjacent_cells


def cavity_map(grid: list[str]) -> list[str]:
    for i in range(len(grid)):
        for j in range(len(grid)):
            current_cell = grid[i][j]
            adjacent_cells = get_adjacent_cells(grid, i, j)
            if "X" not in adjacent_cells:
                if all(
                    int(adjacent_cell) < int(current_cell)
                    for adjacent_cell in adjacent_cells
                ):
                    grid[i] = grid[i][:j] + "X" + grid[i][j + 1 :]
    return grid
