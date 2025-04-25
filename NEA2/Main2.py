from settings2 import *
from Engine2 import Engine
import pygame
import sys
import os
from menu import main_menu

class App:
    def __init__(self):
        pygame.mixer.init()  # Initialize the mixer
        ray.init_window(WIN_WIDTH, WIN_HEIGHT, 'Quest')
        self.dt = 1/60
        self.engine = Engine(app=self)

        # Load background music
        music_path = "background_music.mp3"
        try:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)  # Play the music in a loop
        except pygame.error as e:
            print(f"Unable to load background music: {e}")

    def run(self):
        while not ray.window_should_close():
            self.dt = ray.get_frame_time()
            self.engine.update()
            self.engine.draw()
        #
        ray.close_window()

if __name__ == '__main__':
    if main_menu():  # Show the Pygame menu first
        app = App()
        app.run()