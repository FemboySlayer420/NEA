import pygame
import sys
import os

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((2040, 1080))
    pygame.display.set_caption("Main Menu")

    # Load background image
    background_path = "background.jpg"
    try:
        background = pygame.image.load(background_path)
        background = pygame.transform.scale(background, (2040, 1080))
    except pygame.error as e:
        print(f"Unable to load background image: {e}")
        pygame.quit()
        sys.exit()

    # Load Start Game button image
    start_button_path = "start_button.png"
    try:
        start_button = pygame.image.load(start_button_path)
        start_button = pygame.transform.scale(start_button, (500, 167))
        start_button_rect = start_button.get_rect(center=(1020, 300))
    except pygame.error as e:
        print(f"Unable to load start button image: {e}")
        pygame.quit()
        sys.exit()

    # Load Quit button image
    quit_button_path = "quit_button.png"
    try:
        quit_button = pygame.image.load(quit_button_path)
        quit_button = pygame.transform.scale(quit_button, (500, 167))
        quit_button_rect = quit_button.get_rect(center=(1020, 800))
    except pygame.error as e:
        print(f"Unable to load quit button image: {e}")
        pygame.quit()
        sys.exit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    return True  # Exit the menu and start the game
                elif quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()  # Exit the menu and close the program

        screen.blit(background, (0, 0))
        screen.blit(start_button, start_button_rect)
        screen.blit(quit_button, quit_button_rect)
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()