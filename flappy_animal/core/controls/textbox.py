from flappy_animal.core.wrapper import PyGameWrapper, pygame
from flappy_animal.core.utils import Tuple
class TextBox(object):
    def __init__(self, name: str, text: str, location: Tuple, antialiasing: bool, color: Tuple, font: str, size: bytes) -> None:
        self.name: str = name
        self.text: str = text
        self.location: Tuple = location
        self.antialiasing: bool = antialiasing
        self.color: Tuple = color
        self.font: str = font
        self.size: bytes = size
        self.surface: pygame.Surface = None

    def draw(self) -> None:
        font: pygame.font.Font = PyGameWrapper.set_font(self.font, self.size)
        self.surface = font.render(self.text, self.antialiasing, self.color)

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)
