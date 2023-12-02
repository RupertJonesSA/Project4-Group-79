from sudoku_generator import SudokuGenerator
import sys
from cell import Cell
import pygame as pg

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = SudokuGenerator(SudokuGenerator.row_length, SudokuGenerator.removed_cells)
        self.cells = [[Cell(self.board[row][cols], row, cols, self.screen) for cols in range(9)] for row in range(9)]

    def draw(self):
        self.screen.fill(255, 255, 245)
        for i in range(1, 10):
            if (i == 3 or 6 or 9):
                pg.draw.line(self.screen, (0, 0, 0), (0, i * 100), (900, i * 100), 6)

    def select(self, row, col):
        for i in range(9):
            for j in range(9):
                self.cells[row][col].selected = False

    def click(self, x, y):
        if (x < self.width) and (y < self.height):
            row = y // 100
            col = x // 100
            return (int(row), int(col))
        else:
            return None

    def clear(self):
        self.cells[self.row][self.col].sketch_value = 0
        self.cells[self.row][self.col].value = 0

    def sketch(self, value):
        self.cells[self.row][self.col].set_sketched_value(value)

    def place_number(self, value):
        self.cells[self.row][self.col].set_cell_value(value)


