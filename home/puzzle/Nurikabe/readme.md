### Nurikabe Puzzle

#### [Description of 'Tic-Tac-Logic' rule]

[Description of 'Nurikabe' rules]

* There are numbers in the game, and the meaning of the number is the number of empty spaces including your own square.

* Numbers do not share each other's empty space.

* Except for the empty space, the rest must be filled with walls, and all walls must be connected.

* Walls are not considered to be connected diagonally.

* Walls must not form a 2x2 square.

#### How to use

```shell
git clone this repo
```

```python
from Nurikabe import Nurikabe
print(Nurikabe(7).get_board())
```

```shell
board
    0   1   2   3   4   5   6  
   ------------------------------------
 0 | 5 |   |   |   |   |   |   |
   ------------------------------------
 1 |   |   | 1 |   | 5 |   |   |
   ------------------------------------
 2 |   |   |   |   |   |   |   |
   ------------------------------------
 3 |   |   |   | 6 |   |   |   |
   ------------------------------------
 4 |   |   |   |   |   |   |   |
   ------------------------------------
 5 |   | 1 |   |   |   |   |   |
   ------------------------------------
 6 |   |   |   |   |   |   | 1 |
   ------------------------------------

list of board
[[5, ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 1, ' ', 5, ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 6, ' ', ' ', ' '], [' ', 
' ', ' ', ' ', ' ', ' ', ' '], [' ', 1, ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 1]]
```

```python
from Nurikabe import Nurikabe
print(Nurikabe(7).get_answer())
```

```shell
answer board
    0   1   2   3   4   5   6  
   ------------------------------------
 0 | X | X | 0 | X | X | X | 0 |
   ------------------------------------
 1 | 0 | X | X | X | 0 | X | 0 |
   ------------------------------------
 2 | X | 0 | X | 0 | 0 | X | X |
   ------------------------------------
 3 | X | X | X | 0 | 0 | 0 | X |
   ------------------------------------
 4 | X | 0 | X | X | X | X | X |
   ------------------------------------
 5 | X | 0 | X | 0 | 0 | 0 | X |
   ------------------------------------
 6 | X | X | X | X | X | X | X |
   ------------------------------------

region of not wall
[[(0, 2)], [(0, 6), (1, 6)], [(1, 0)], [(1, 4), (2, 4), (3, 4), (3, 5), (3, 3), (2, 3)], [(2, 1)], [(4, 1), (5, 1)], [(5, 3), (5, 4), (5, 5)]]
```

enjoy!