from flappy_animal.core.commons import os
from flappy_animal.core.wrapper import PyGameWrapper

class Window:
    def __init__(self, width, height, handler) -> None:
        self.width = width
        self.height = height
        self.handler = handler
        self.window = PyGameWrapper.display_set_mode(self.width, self.height)

    @staticmethod
    def update():
        PyGameWrapper.update()

    @staticmethod
    def flip():
        PyGameWrapper.display_flip()

    @staticmethod
    def caption(text):
        PyGameWrapper.display_set_caption(text)

    def blit(self, surface, location):
        self.window.blit(surface, location)

    def set_background(self, color=None, image=None):

        if color is not None:
            self.window.fill(color)

        elif image is not None:
            bg = PyGameWrapper.image_load(os.path.join("flappy_animal/assets/images/backgrounds", image))
            PyGameWrapper.scale(bg, (self.width, self.height))
            self.window.blit(bg, (0,0))
            return bg
