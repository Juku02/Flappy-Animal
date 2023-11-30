from floppy_animal.core.wrapper import PyGameWrapper

class Window:
    def __init__(self, width, heigth) -> None:
        self.width = width
        self.heigth = heigth
        self.screen = PyGameWrapper.display_set_mode(self.width, self.heigth)   
        
    def fill(self, color):
       self.screen.fill(color)
        
    def flip(self):
        PyGameWrapper.display_flip()