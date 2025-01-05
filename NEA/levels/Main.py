from settings import *
from Engine import Engine

class App:
    ray.init_window(WIN_WIDTH, WIN_HEIGHT, 'GAME')
    
    def __init__(self):
        self.dt = 1/60
        self.engine = Engine(app=self)
    
    def run(self):
        while not ray.window_should_close():
            self.dt = ray.get_frame_time()
            self.engine.update()
            self.engine.draw()
        #
        ray.close_window()

if __name__ == '__main__':
    app = App()
    app.run()