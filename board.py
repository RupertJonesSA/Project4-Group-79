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
        self.answer, self.original_board = generate_sudoku(9, difficulty)
        self.used_board = [[c for c in self.original_board[r]] for r in range(len(self.original_board))]
        # Allocates value and "generated" boolean value based on self.board to each cell object 
        self.cells = [[Cell(self.original_board[row][cols], row, cols, self.screen, 1 if self.original_board[row][cols] != 0 else 0) 
                       for cols in range(9)] for row in range(9)]

    def draw(self):
        self.screen.fill(pg.Color("DarkRed"))
        margin = 0
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
        # Deselect the one that is currently selected (if there is one)
        for r in self.cells:
            for c in r:
                if c.selected:
                    c.selected = 0
        self.cells[row][col].selected = 0 if self.cells[row][col].answered else 1

    def click(self, x, y):
        if (x < self.width) and (y < self.height):
            row = y // 100
            col = x // 100
            return (int(row), int(col))
        else:
            return None

    def clear(self, row, col):
        # If selected cell is not a generated cell or already answered, clear cell values
        if(not self.cells[row][col].generated and not self.cells[row][col].answered):
            self.cells[row][col].sketch_value = 0
            self.cells[row][col].value = 0

    def sketch(self, value, row, col):
        if(not self.cells[row][col].generated and not self.cells[row][col].answered):
            self.cells[row][col].set_sketched_value(value)

    def place_number(self, row, col):
        if(not self.cells[row][col].generated and not self.cells[row][col].answered):
            value = self.cells[row][col].sketch_value
            self.cells[row][col].set_sketched_value(0)
            self.cells[row][col].set_cell_value(value)
            # Makes the answered cell unable to be altered or selected
            self.cells[row][col].answered = 1

    def reset_to_original(self):
       # Turn all values of cell back to the original 
       self.cells = [[Cell(self.original_board[row][cols], row, cols, self.screen, 1 if self.original_board[row][cols] != 0 else 0) 
                      for cols in range(9)] for row in range(9)] 
        

    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.used_board[i][j] == 0:
                    return False
        return True

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.used_board[i][j] = self.cells[i][j].value

    def check_board(self):
        for r in range(9):
            for c in range(9):
                if (self.used_board[r][c] != self.answer[r][c]):
                    return False
        return True
