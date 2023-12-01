"""
Class created by Sami Al-Jamal

Reference: https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/#
"""

import pygame as pg

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = 0
    
    def draw(self, surface):
        action = 0
        # Get mouse position
        pos = pg.mouse.get_pos()

        # Check mouseover and clicked eventlistener
        if (self.rect.collidepoint(pos)):
            # If left-clicked
            if (pg.mouse.get_pressed()[0] and self.clicked == 0):
                self.clicked = 1
                action = 1
        
        if (pg.mouse.get_pressed()[0] == 0):
            self.clicked = 0

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action