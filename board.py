from sudoku_generator import generate_sudoku
import sys
from cell import Cell
import pygame as pg

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.answer, self.board = generate_sudoku(9, difficulty)
        self.cells = [[Cell(self.board[row][cols], row, cols, self.screen) for cols in range(9)] for row in range(9)]

    def draw(self):
        self.screen.fill(pg.Color("DarkRed"))
        margin = 2
        # Draw rectangle/square based on width and height attributes
        pg.draw.rect(self.screen, pg.Color("black"), pg.Rect(margin, margin, self.width - margin*2, self.height - margin*2), 10)
        
        # Iterates based on the dimensions (self.height and self.width). Draws 9 horizontal and 9 vertical lines
        i = 1
        while (i * 100) < self.height - 30:
            line_width = 5 if i % 3 > 0 else 10
            pg.draw.line(self.screen, pg.Color("black"), pg.Vector2((i * 100) + margin, margin), pg.Vector2((i * 100) + margin, self.width - margin), line_width)
            pg.draw.line(self.screen, pg.Color("black"), pg.Vector2(margin, (i * 100) + margin), pg.Vector2(self.height - margin, (i * 100) + margin), line_width)
            i += 1 
        
        for row in self.cells:
            for col in row:
                col.draw()

    def select(self, row, col):
        self.cells[row][col].selected = 1

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

    def reset_to_original(self):
        self.cells = [[Cell(self.board[row][cols], row, cols, self.screen) for cols in range(9)] for row in range(9)]

    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return False
        return True

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.cells[i][j].value

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == None:
                    return True
        return False

    def check_board(self):
        for i in range(9):
            for j in range(9):
                if not self.is_valid(i, j, self.board[i][j]):
                    return False
        return True
