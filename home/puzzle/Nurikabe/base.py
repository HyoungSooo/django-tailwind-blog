import random
import copy


class Nurikabe:
    def __init__(self, cell) -> None:
        self.map = None
        self.cell = cell
        self.__check_input()
        self.__create_map()
        self.__fill_blanks()
        self.answer = self.__find_zero_regions()
        self.before_map = copy.deepcopy(self.map)
        self.__map()

    def __check_input(self):
        if self.cell not in [5, 7, 9, 11]:
            raise ValueError('Puzzle Size must be in [5,7,9,11]')

    def __create_map(self):
        self.map = [[0 for i in range(self.cell)] for i in range(self.cell)]

    def __find_zero_regions(self):
        grid = copy.deepcopy(self.map)

        def dfs(row, col, region):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 0:
                return
            grid[row][col] = -1  # Mark as visited
            region.append((row, col))
            dfs(row + 1, col, region)
            dfs(row - 1, col, region)
            dfs(row, col + 1, region)
            dfs(row, col - 1, region)

        zero_regions = []
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] == 0:
                    region = []
                    dfs(row, col, region)
                    if region:
                        zero_regions.append(region)

        if len(max(zero_regions, key=lambda x: len(x))) > 8:
            self.__fill_blanks(False, max(zero_regions, key=lambda x: len(x)))
            return

        return zero_regions

    def __check_vaildation(self, row, col):
        check_square = [
            [(0, -1), (1, 0), (1, -1)],
            [(0, -1), (-1, 0), (-1, -1)],
            [(0, 1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 0), (1, 1)],
        ]
        for i in range(len(check_square)):
            set_symbols = set(['X'])
            for x_move, y_move in check_square[i]:

                if 0 <= row + x_move < self.cell and 0 <= col + y_move < self.cell:
                    set_symbols.add(
                        self.map[row + x_move][col + y_move])
                else:
                    break
            else:
                if len(set_symbols) == 1:
                    break
        else:
            if self.map[row][col] != 'X':
                return True, (row, col)

        return False, (0, 0)

    def __fill_blanks(self, start=True, region=None):
        if start:
            start_point = random.randint(0, self.cell-1)

            stack = [(0, start_point)]
        else:
            while True:
                start_point = random.choice(region)
                flag, start = self.__check_vaildation(
                    start_point[0], start_point[1])

                if flag:
                    stack = [start]
                    break

                region.remove(start_point)
        while stack:
            row, col = stack.pop()

            self.map[row][col] = 'X'

            symbols = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while True:
                if not symbols:
                    self.__find_zero_regions()
                    return

                symbol = random.choice(symbols)

                if 0 <= row + symbol[0] < self.cell and 0 <= col + symbol[1] < self.cell:
                    flag, moves = self.__check_vaildation(
                        row + symbol[0], col + symbol[1])

                    if flag:
                        stack.append(moves)
                        break

                symbols.remove(symbol)

    def __map(self):
        regions = self.__find_zero_regions()

        for region in regions:
            start_point = region[0]

            for x, y in region:
                self.map[x][y] = 0

            self.map[start_point[0]][start_point[1]] = len(region)

        for row in range(self.cell):
            for col in range(self.cell):
                if self.map[row][col] == 'X':
                    self.map[row][col] = 0

    def print_board(self, before=False):
        if before:
            map = self.before_map
        else:
            map = self.map
        rows = len(map)
        cols = len(map[0])

        print('   ', end='')
        for col in range(cols):
            print(f'{col:2}', end='  ')
        print('\n   ' + '-' * (cols * 5 + 1))

        for row in range(rows):
            print(f'{row:2} |', end=' ')
            for cell in map[row]:
                print(cell, end=' | ')
            print('\n   ' + '-' * (cols * 5 + 1))

    def get_board(self):
        self.print_board()
        return self.map

    def get_answer(self):
        self.print_board(True)
        return self.answer


print(Nurikabe(7).get_board())
