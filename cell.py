# Class created by Rogeh Beshay
import pygame as pg

class Cell:

    def __init__(self, value, row, col, screen, generated=0):
        self.selected = 0
        self.answered = 0
        self.generated = generated
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
        if self.selected:
            pg.draw.rect(self.screen, "darkorchid1", pg.Rect(self.col * 83, self.row * 83, 83, 83), 6)

        if (self.sketch_value != 0) and (self.value == 0):
            font = pg.font.Font('assets/fonts/OldeEnglish.ttf', 75)
            surface = font.render(str(self.sketch_value), 0, (100, 100, 100))
            rectangle = surface.get_rect(center=(self.col * 83 + 20, self.row * 83 + 30))
            self.screen.blit(surface, rectangle)
         
        elif (self.value != 0) and (self.sketch_value == 0):
            font = pg.font.Font('assets/fonts/OldeEnglish.ttf', 100)
            surface = font.render(str(self.value), 0, (0, 0, 0))
            rectangle = surface.get_rect(center=(self.col * 83 + 41, self.row * 83 + 45))
            self.screen.blit(surface, rectangle)

        elif (self.value != 0) and (self.sketch_value != 0):
            font = pg.font.Font('assets/fonts/OldeEnglish.ttf', 100)
            surface = font.render(str(self.value), 0, (128, 128, 128))
            rectangle = surface.get_rect(center=(self.col * 83 + 41, self.row * 83 + 45))
            self.screen.blit(surface, rectangle)
