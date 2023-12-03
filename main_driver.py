import pygame as pg
from sudoku_generator import generate_sudoku
from board import Board
from button import Button
import sys 

pg.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 1000

SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

BG = pg.image.load('assets/real_background.png').convert_alpha()
# src: https://www.google.com/url?sa=i&url=https%3A%2F%2Ftwitter.com%2FPinkySoulOG%2Fstatus%2F1624928442339717128&psig=
#      AOvVaw1rC3LoDn4R5d7KORUwcnQ9&ust=1701483433610000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOjTze-V7YIDFQAAAAAdAAAAABAE
EASY_IMAGE = pg.image.load('assets/easy.png').convert_alpha()
NORMAL_IMAGE = pg.image.load('assets/normal.png').convert_alpha()
HARD_IMAGE = pg.image.load('assets/hard.png').convert_alpha()
RESET_IMAGE = pg.image.load('assets/reset.png').convert_alpha()
RESTART_IMAGE = pg.image.load('assets/restart.png').convert_alpha()
EXIT_IMAGE = pg.image.load('assets/exit.png').convert_alpha()


MENU_FONT = pg.font.Font(None, 80)
SUB_FONT = pg.font.Font(None, 70)

# Runs playable sudoku board
def play(game_board):
    pg.display.set_caption("Play")
    SCREEN.fill("black")
    
    game_board.update_board()
    game_board.draw()

    # Bottom Menu Buttons
    RESET_BUTTON = Button(100, 910, RESET_IMAGE, 0.15)
    RESTART_BUTTON = Button(325, 910, RESTART_IMAGE, 0.15)
    CLEAR_BUTTON = Button(550, 910, EXIT_IMAGE, 0.15)
    
    RESET_BUTTON.draw(SCREEN)
    RESTART_BUTTON.draw(SCREEN)
    CLEAR_BUTTON.draw(SCREEN)


def main():
    pg.display.set_caption("Menu")
    BACKGROUND = pg.transform.scale(BG, (int(BG.get_width() * 3.35), int(BG.get_height() * 3.3)))
    SCREEN.blit(BACKGROUND, (-60, -50))
    #SCREEN.fill("brown")
    TITLE_TEXT = MENU_FONT.render("Welcome to Sudoku", 1, "brown3")
    TITLE_RECT = TITLE_TEXT.get_rect(center=(SCREEN_WIDTH // 2, 225))
    SUB_TEXT = SUB_FONT.render("Select game mode", 1, "brown3")
    SUB_RECT = SUB_TEXT.get_rect(center=(SCREEN_WIDTH//2, 400))
    SCREEN.blit(TITLE_TEXT, TITLE_RECT)
    SCREEN.blit(SUB_TEXT, SUB_RECT)

    EASY_BUTTON = Button(220, 650, EASY_IMAGE, 0.6)
    NORMAL_BUTTON = Button(370, 650, NORMAL_IMAGE, 0.6)
    HARD_BUTTON = Button(520, 650, HARD_IMAGE, 0.6)

    run = 1
    difficulty = ""
    played = 0 
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
            # Checks to see if a board already has been generated
            if(not played):
                removed = 0
                # Bases amount removed on user difficulty input
                if(difficulty == "easy"): removed = 30
                elif(difficulty == "medium"): removed = 40
                else: removed = 50
                # Creates Board object (minus height by 200 to leave remove on the bottom for other three buttons)
                game_board = Board(SCREEN_WIDTH, SCREEN_HEIGHT - 100, SCREEN, removed)
                # For debugging purposes (not permanent) 
                # for r in game_board.board:
                #     for c in r:
                #         print(c, end=" ")
                #     print()
                played = 1
            play(game_board)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = 0
        pg.display.update()
    pg.quit() 


if __name__ == "__main__":
    main()