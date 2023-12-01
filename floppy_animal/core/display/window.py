from floppy_animal.core.wrapper import PyGameWrapper

class Window:
    def __init__(self, width, heigth) -> None:
        self.width = width
        self.heigth = heigth
        self.screen = PyGameWrapper.display_set_mode(self.width, self.heigth)   
        
    def flip(self):
        PyGameWrapper.display_flip()
    
    def set_background(self, color=None, image=None):
        if color is not None:
            self.screen.fill(color)
        elif image is not None:
            bg = PyGameWrapper.bg_image_load(image)
            self.screen.blit(bg,(0,0))