## Conways Game Of Life in Python
# Features
* GUI
* OOP
* Board
* Cells
* Seed

# Rules
2D Grid of square cells, each of which has two possible states:
* Alive
* Dead

Each cell interacts with its eight nighbours. 
At time tick N the following transistions occur:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# Classes
Life 
* Initial Setup of Universe State (Size, Seed, Ticks)
* Holds State of Universe 
* Time ticks
* Made up of NxM cells

Cells
* Holds Dead/Alive State
* Current and Next State
* Holds State of neighbours