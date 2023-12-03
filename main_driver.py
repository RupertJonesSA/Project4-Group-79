# Main driver made by Sami Al-Jamal
import pygame as pg
from sudoku_generator import generate_sudoku
from board import Board
from button import Button
import sys 

pg.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 1000

SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

BG = pg.image.load('assets/pictures/real_background.png').convert_alpha()
# src: https://www.google.com/url?sa=i&url=https%3A%2F%2Ftwitter.com%2FPinkySoulOG%2Fstatus%2F1624928442339717128&psig=
#      AOvVaw1rC3LoDn4R5d7KORUwcnQ9&ust=1701483433610000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOjTze-V7YIDFQAAAAAdAAAAABAE

# Loading in all the assets and images to be used in the program
EASY_IMAGE = pg.image.load('assets/pictures/easy.png').convert_alpha()
NORMAL_IMAGE = pg.image.load('assets/pictures/normal.png').convert_alpha()
HARD_IMAGE = pg.image.load('assets/pictures/hard.png').convert_alpha()
RESET_IMAGE = pg.image.load('assets/pictures/reset.png').convert_alpha()
RESTART_IMAGE = pg.image.load('assets/pictures/restart.png').convert_alpha()
EXIT_IMAGE = pg.image.load('assets/pictures/exit.png').convert_alpha()
WINNER_IMAGE = pg.image.load('assets/pictures/winner.png').convert_alpha()
LOSER_IMAGE = pg.image.load('assets/pictures/loser.png').convert_alpha()

MENU_FONT = pg.font.Font('assets/fonts/Deadwax Extreme DEMO.ttf', 90)
SUB_FONT = pg.font.Font('assets/fonts/Deadwax Hard DEMO.ttf', 70)
END_FONT = pg.font.Font('assets/fonts/Deadwax DEMO.ttf', 110)

# Runs playable sudoku board
def play(game_board):
    pg.display.set_caption("Play")
    SCREEN.fill("black")
    
    # Uncomment if you want to see the answer key
    # for r in game_board.answer:
    #     for c in r:
    #         print(c, end=" ")
    #     print()
    # Keeps track of selected cell

    curr_row = 0
    curr_col = 0
    while 1:
        game_board.draw()

        # Bottom Menu Buttons
        RESET_BUTTON = Button(100, 910, RESET_IMAGE, 0.15)
        RESTART_BUTTON = Button(325, 910, RESTART_IMAGE, 0.15)
        EXIT_BUTTON = Button(550, 910, EXIT_IMAGE, 0.15)
        
        if RESET_BUTTON.draw(SCREEN):
            game_board.reset_to_original()
        if RESTART_BUTTON.draw(SCREEN):
            menu()
        if EXIT_BUTTON.draw(SCREEN):
            pg.quit()
            sys.exit()

        for event in pg.event.get():
            # Indicates that the current cell is selected
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if(game_board.click(pos[0], pos[1]) != None):
                    row, col = game_board.click(pos[0], pos[1])
                    game_board.select(row, col)
                    curr_row = row
                    curr_col = col

            if event.type == pg.KEYDOWN:

                # Moves selector window accordingly to arrow key presses
                if event.key == pg.K_UP:
                    curr_row -= 1 if curr_row > 0 else 0
                    game_board.select(curr_row, curr_col)
                elif event.key == pg.K_RIGHT:
                    curr_col += 1 if curr_col < 8 else 0
                    game_board.select(curr_row, curr_col)
                elif event.key == pg.K_DOWN:
                    curr_row += 1 if curr_row < 8 else 0
                    game_board.select(curr_row, curr_col)
                elif event.key == pg.K_LEFT:
                    curr_col -= 1 if curr_col > 0 else 0
                    game_board.select(curr_row, curr_col)

                # Updates board value based on key pressed
                if event.key == pg.K_1:
                    game_board.sketch(1, curr_row, curr_col)
                elif event.key == pg.K_2:
                    game_board.sketch(2, curr_row, curr_col)
                elif event.key == pg.K_3:
                    game_board.sketch(3, curr_row, curr_col)
                elif event.key == pg.K_4:
                    game_board.sketch(4, curr_row, curr_col)
                elif event.key == pg.K_5:
                    game_board.sketch(5, curr_row, curr_col)
                elif event.key == pg.K_6:
                    game_board.sketch(6, curr_row, curr_col)
                elif event.key == pg.K_7:
                    game_board.sketch(7, curr_row, curr_col)
                elif event.key == pg.K_8:
                    game_board.sketch(8, curr_row, curr_col)
                elif event.key == pg.K_9:
                    game_board.sketch(9, curr_row, curr_col)
                elif event.key == pg.K_BACKSPACE:
                    game_board.clear(curr_row, curr_col)
                elif event.key == pg.K_RETURN:
                    game_board.place_number(curr_row, curr_col)

            game_board.update_board()

            # Check if the board is complete and correct
            if game_board.is_full():
                if game_board.check_board():
                    # Redirect to win screen
                    winner_screen()
                else:
                    # Redirect to lose screen
                    loser_screen()

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()

def winner_screen():
    pg.display.set_caption("WINNER")
    SCREEN.fill("black")
    BACKGROUND = pg.transform.scale(WINNER_IMAGE, (int(WINNER_IMAGE.get_width() * 1.3), int(WINNER_IMAGE.get_height() * 1.3)))
    SCREEN.blit(BACKGROUND, (0, 0))

    TITLE_TEXT = END_FONT.render("Game Won!", 1, "black")
    TITLE_RECT = TITLE_TEXT.get_rect(center=(SCREEN_WIDTH // 2, 75))
    SCREEN.blit(TITLE_TEXT, TITLE_RECT)
    EXIT_BUTTON = Button((SCREEN_WIDTH // 2) - 145, (SCREEN_HEIGHT // 2) - 200, EXIT_IMAGE, 0.2)

    while 1:
        if EXIT_BUTTON.draw(SCREEN):
            pg.quit()
            sys.exit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()

def loser_screen():
    pg.display.set_caption("LOSER")
    SCREEN.fill("black")
    BACKGROUND = pg.transform.scale(LOSER_IMAGE, (int(LOSER_IMAGE.get_width() * 1.3), int(LOSER_IMAGE.get_height() * 1.3)))
    SCREEN.blit(BACKGROUND, (0, 0))

    TITLE_TEXT = END_FONT.render("Game OVER ;(", 1, "black")
    TITLE_RECT = TITLE_TEXT.get_rect(center=(SCREEN_WIDTH // 2, 75))
    SCREEN.blit(TITLE_TEXT, TITLE_RECT)

    RESTART_BUTTON = Button((SCREEN_WIDTH // 2) - 145, (SCREEN_HEIGHT // 2) - 200, RESTART_IMAGE, 0.2)

    while 1:
        if RESTART_BUTTON.draw(SCREEN):
            menu()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()
                

def menu():
    pg.display.set_caption("Menu")
    BACKGROUND = pg.transform.scale(BG, (int(BG.get_width() * 3.35), int(BG.get_height() * 3.3)))
    SCREEN.blit(BACKGROUND, (-60, -50))
    
    TITLE_TEXT = MENU_FONT.render("Welcome to Sudoku", 1, "brown3")
    TITLE_RECT = TITLE_TEXT.get_rect(center=(SCREEN_WIDTH // 2, 225))
    SUB_TEXT = SUB_FONT.render("Select game mode", 1, "brown3")
    SUB_RECT = SUB_TEXT.get_rect(center=(SCREEN_WIDTH//2, 400))
    SCREEN.blit(TITLE_TEXT, TITLE_RECT)
    SCREEN.blit(SUB_TEXT, SUB_RECT)

    EASY_BUTTON = Button(130, 650, EASY_IMAGE, 0.17)
    NORMAL_BUTTON = Button(355, 650, NORMAL_IMAGE, 0.17)
    HARD_BUTTON = Button(580, 650, HARD_IMAGE, 0.17)

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
                # Creates Board object (minus height by 100 to leave remove on the bottom for other three buttons)
                game_board = Board(SCREEN_WIDTH, SCREEN_HEIGHT - 100, SCREEN, removed)
                played = 1
                play(game_board)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = 0
        pg.display.update()
    pg.quit() 


if __name__ == "__main__":
    menu()