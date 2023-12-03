# Class created by Rogeh Beshay
import pygame as pg

class Cell:

    def __init__(self, value, row, col, screen):
        self.initial = False
        self.selected = False
        self.chosen = False
        self.sketch_value = 0
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketch_value = value

    def draw(self):
        if self.chosen == False:
            pg.draw.rect(self.screen, (255, 0, 0), pg.Rect(self.col * 100, self.row * 100, 100, 100), 6)

        if (self.sketch_value != 0) and (self.value == 0):
            font = pg.font.Font(None, 75)
            surface = font.render(str(self.sketch_value), 0, (100, 100, 100))
            rectangle = surface.get_rect(center=(self.col * 100 + 50, self.row * 100 + 50))
            self.screen.blit(surface, rectangle)
         
        elif (self.value != 0) and (self.sketch_value == 0):
            font = pg.font.Font(None, 125)
            surface = font.render(str(self.value), 0, (0, 0, 0))
            rectangle = surface.get_rect(center=(self.col * 100 + 50, self.row * 100 + 50))
            self.screen.blit(surface, rectangle)

        elif (self.value != 0) and (self.sketch_value != 0):
            font = pg.font.Font(None, 125)
            surface = font.render(str(self.value), 0, (128, 128, 128))
            rectangle = surface.get_rect(center=(self.col * 100 + 50, self.row * 100 + 50))
            self.screen.blit(surface, rectangle)
