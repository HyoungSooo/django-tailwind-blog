import random
from collections import Counter
import time
import copy
import sys


class TicTacLogic:
    def __init__(self, cell, blank) -> None:
        self.cell = cell
        self.blank = blank
        self.blank_dict = {}
        self.map = []
        self.kernal_size = 3

        self.__check_input()

        self.__create_map_base_cell()

        self.__create_puzzle()

    def __check_input(self):
        if self.cell < 5:
            raise ValueError('cell must be more then five')

        if self.blank > self.cell ** 2:
            raise ValueError('blank must be smaller than cell ** 2')

        if self.cell % 2 != 0:
            raise ValueError('cell must be a even number')

    def __create_map_base_cell(self):
        self.map = [[0 for _ in range(self.cell)] for _ in range(self.cell)]

    def __create_puzzle(self):
        def run():
            symbols = ['X', 'O']
            for row in range(self.cell):
                for col in range(self.cell):
                    remaining_symbols = symbols.copy()
                    while True:
                        if not remaining_symbols:
                            return False
                        symbol = random.choice(remaining_symbols)
                        if not self.__check_validations(row, col, symbol):
                            self.map[row][col] = symbol
                            break
                        remaining_symbols.remove(symbol)
            return True
        while True:
            t = run()
            if t:
                break
            else:
                self.__create_map_base_cell()

        self.__create_blank()
        return self.map

    def __check_validations(self, row, col, symbol):
        val = [
            [(0, 1), (0, -1)],
            [(1, 0), (-1, 0)],
            [(0, 1), (0, 2)],
            [(0, -1), (0, -2)],
            [(1, 0), (2, 0)],
            [(-1, 0), (-2, 0)],
        ]
        self.map[row][col] = symbol
        col_counter = Counter([self.map[i][col] for i in range(self.cell)])

        row_symbol = Counter(self.map[row])

        if col_counter[symbol] > self.cell // 2 or row_symbol[symbol] > self.cell // 2:
            self.map[row][col] = 0
            return True

        position_list = []

        for location in val:
            ls = [self.map[row][col]]
            for x, y in location:
                try:
                    if 0 <= row + y < self.cell and 0 <= col + x < self.cell:
                        ls.append(self.map[row + y][col + x])
                    else:
                        break
                except IndexError:
                    break
            else:
                position_list.append(ls)

        for validation in position_list:
            if all(validation[i] == symbol for i in range(3)):
                return True

        return False

    def __print_board(self):
        rows = len(self.map)
        cols = len(self.map[0])

        print('   ', end='')
        for col in range(cols):
            print(f'{col:2}', end='  ')
        print('\n   ' + '-' * (cols * 5 + 1))

        for row in range(rows):
            print(f'{row:2} |', end=' ')
            for cell in self.map[row]:
                print(cell, end=' | ')
            print('\n   ' + '-' * (cols * 5 + 1))

    def __print_coordinates(self):
        for key in self.blank_dict:
            x, y = key.split()
            print(f"({x}, {y})")

    def __create_blank(self):
        count = 0

        if not self.blank:
            return
        while count <= self.blank:
            x, y = random.randint(
                0, self.cell - 1), random.randint(0, self.cell - 1)

            if self.map[x][y] == ' ':
                continue

            self.map[x][y] = ' '
            self.blank_dict[' '.join([str(x), str(y)])] = ' '
            count += 1

    def run(self):
        saved_map = copy.deepcopy(self.map[:])
        while True:
            self.__print_board()
            answer = input()

            if answer == 'd':
                for row in range(self.cell):
                    flag = True
                    for col in range(self.cell):
                        is_ok = self.__check_validations(
                            row, col, self.map[row][col])

                        if is_ok:
                            print('wrong answer')
                            flag = False
                            break
                    if not flag:
                        time.sleep(1)
                        break
                else:
                    print('good job')
                    return
            elif answer == 'f':
                print('format the puzzle')
                self.map = copy.deepcopy(saved_map[:])
            elif answer == 'b':
                print('blank location')
                self.__print_coordinates()
            else:
                try:
                    symbol, y, x = answer.strip().split(' ')

                    if symbol not in ['X', 'O']:
                        print('unvaild input')
                        continue

                    if ' '.join([y, x]) not in self.blank_dict:
                        print('You cannot edit tiles that were not empty')
                        continue

                    self.map[int(y)][int(x)] = symbol
                except IndexError:
                    print('unvaild location')
                except:
                    print('unvaild input')


list_argv = sys.argv


TicTacLogic(int(list_argv[1]), int(list_argv[2])).run()
