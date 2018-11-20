import pygame
from settings import Settings
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Quiz Game")

    # Create scoreboard
    sb = Scoreboard(ai_settings, screen)

    # Make a button
    button = Button(screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, button, sb)
        gf.update_screen(ai_settings, screen, button, sb)

run_game()

#  Question and answer source : https://www.sanfoundry.com/1000-python-questions-answers/