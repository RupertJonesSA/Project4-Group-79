import pygame as pg
from button import Button
import sys 

pg.init()
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 800

SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

BG = pg.image.load('assets/real_background.png').convert_alpha()
# src: https://www.google.com/url?sa=i&url=https%3A%2F%2Ftwitter.com%2FPinkySoulOG%2Fstatus%2F1624928442339717128&psig=
#      AOvVaw1rC3LoDn4R5d7KORUwcnQ9&ust=1701483433610000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOjTze-V7YIDFQAAAAAdAAAAABAE
EASY_IMAGE = pg.image.load('assets/easy.png').convert_alpha()
NORMAL_IMAGE = pg.image.load('assets/normal.png').convert_alpha()
HARD_IMAGE = pg.image.load('assets/hard.png').convert_alpha()

MENU_FONT = pg.font.Font(None, 80)
SUB_FONT = pg.font.Font(None, 70)

# Runs playable sudoku board
def play(mode):
    pg.display.set_caption("Play")
    SCREEN.fill("black")
    # Need board and cell class to finish this hoe (please)


def main():
    pg.display.set_caption("Menu")
    BACKGROUND = pg.transform.scale(BG, (int(BG.get_width() * 2.5), int(BG.get_height() * 2.5)))
    SCREEN.blit(BACKGROUND, (0, -50))
    #SCREEN.fill("brown")
    TITLE_TEXT = MENU_FONT.render("Welcome to Sudoku", 1, "brown3")
    TITLE_RECT = TITLE_TEXT.get_rect(center=(SCREEN_WIDTH // 2, 125))
    SUB_TEXT = SUB_FONT.render("Select game mode", 1, "brown3")
    SUB_RECT = SUB_TEXT.get_rect(center=(SCREEN_WIDTH//2, 300))
    SCREEN.blit(TITLE_TEXT, TITLE_RECT)
    SCREEN.blit(SUB_TEXT, SUB_RECT)

    EASY_BUTTON = Button(150, 500, EASY_IMAGE, 0.6)
    NORMAL_BUTTON = Button(300, 500, NORMAL_IMAGE, 0.6)
    HARD_BUTTON = Button(450, 500, HARD_IMAGE, 0.6)

    run = 1
    difficulty = ""
    while(run):
        # Menu button event
        if (EASY_BUTTON.draw(SCREEN) and len(difficulty) == 0):
            difficulty = "easy"
        if(NORMAL_BUTTON.draw(SCREEN) and len(difficulty) == 0):
            difficulty = "medium"
        if (HARD_BUTTON.draw(SCREEN) and len(difficulty) == 0): 
            difficulty = "hard"
        
        # Run play screen
        if(len(difficulty) != 0):
            play(difficulty)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = 0
        pg.display.update()
    pg.quit() 


if __name__ == "__main__":
    main()