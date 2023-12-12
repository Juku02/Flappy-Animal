from floppy_animal.core.wrapper import PyGameWrapper
from floppy_animal.core.commons import os

class Window:
    def __init__(self, width, heigth) -> None:
        self.width = width
        self.heigth = heigth
        self.window = PyGameWrapper.display_set_mode(self.width, self.heigth)
        
    def update(self):
        PyGameWrapper.update()
        
    def flip(self):
        PyGameWrapper.display_flip()

    def blit(self, surface, location):
        self.window.blit(surface, location)
    
    def set_background(self, color=None, image=None):
        if color is not None:
            self.window.fill(color)
            
        elif image is not None:
            bg = PyGameWrapper.bg_image_load(os.path.join("floppy_animal/image", image))
            self.window.blit(bg,(0,0))
