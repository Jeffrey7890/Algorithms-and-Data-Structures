## Conway's Game of Life using sparse matrix 😄

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, 
live or dead (or populated and unpopulated, respectively). 
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.
Each cell follow a specific set of rules which are:\
\
👉 Any live cell with two or three live neighbours survives.\
👉 Any dead cell with three live neighbours becomes a live cell.\
👉 All other live cells die in the next generation. Similarly, all other dead cells stay dead.

An infinite two-dimensional grid of sqaure cell can be implimented using a sparse matrix.

The the sparseGameVisual.py can be configured through command line:\
$ python sparseGameVisual.py [(1,2),(2,1),(4,3)]\
$ python sparseGameVisual.py configuration_name (either slider gun or LWS)
  
Currently there are only two configuration in the configuration.py\
🔲Light weight space ship, command LWS\
🔲Slider gun

You can add more configurations if you want, and feel free to adjust the screen with and height\
its kind of slow though 😞, if you have any ideas to make it faster when drawing please help\
anyways have fun 😸

## Prerequisite
pygame
installation:\
$ pip install pygame

