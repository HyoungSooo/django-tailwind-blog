### Tic Tac Toe Logic Puzzle

#### [Description of 'Tic-Tac-Logic' rule]

* There are O and X in the game, and three O or X cannot be connected horizontally or vertically.

* It doesn't matter if there are more than three in a row diagonally.

* The O's and X's in each row and column are no more than half the size of the puzzle.

#### How to use

* clone this repository

in terminal

```shell
python base.py 8 10
```

* first argument (7) is size of the puzzle
* The second argument (10) determines how many blanks there are in the puzzle.


* result
![화면 캡처 2023-08-11 154408](https://github.com/HyoungSooo/pychess-assitance/assets/86239441/8f31ca01-e8c6-43ba-9588-0ec469181148)

#### command
* 'd' => Command to check if puzzle is correct
* 'f' => Command to reset the puzzle
* 'b' => Command that returns the coordinates where there was an existing blank
* 'X x_pos y_pos => (ex 'X 0 1' or 'O 1 2) => Command to fill in the blanks

example fill the blank

![image](https://github.com/HyoungSooo/pychess-assitance/assets/86239441/21faddda-7a77-4226-bb0e-1f47e0215f0f)

You can see that the blank space of the coordinates of 3 and 0 is filled with the entered symbol.

enjoy!
