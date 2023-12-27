from flappy_animal.core.wrapper import PyGameWrapper
class TextBox(object):
    def __init__(self, name, text, location, antialiasing, color, font, size):
        self.name = name
        self.text = text
        self.location = location
        self.antialiasing = antialiasing
        self.color = color
        self.font = font
        self.size = size
        self.surface = None

    def draw(self):
        font = PyGameWrapper.set_font(self.font, self.size)
        self.surface = font.render(self.text, self.antialiasing, self.color)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)