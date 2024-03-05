**Project Name: Island Perimeter Calculator**

**Description:**
This project provides a Python function to calculate the perimeter of an island represented by a 2D grid. The grid consists of cells where 1s represent land and 0s represent water. The function iterates through the grid, counting the perimeter of the island based on adjacent cells. The perimeter of the island is returned as the output.

**How It Works:**
- **island_perimeter(grid)**:
  - This function takes a 2D grid as input, where each cell is either 0 or 1.
  - It iterates through each cell of the grid.
  - For each land cell (1), it counts the perimeter based on adjacent cells.
  - If the cell is on the edge of the grid or adjacent to water (0), it adds to the perimeter.
  - If the cell is adjacent to another land cell, it doesn't add to the perimeter.
  - Finally, the total perimeter of the island is returned.

**Example Usage:**
```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
perimeter = island_perimeter(grid)
print("Perimeter of the island:", perimeter)
```

**Sample Output:**
```
Perimeter of the island: 16
```

**Constraints:**
- The grid is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
