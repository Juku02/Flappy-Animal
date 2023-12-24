from flappy_animal.core.wrapper import PyGameWrapper
from flappy_animal.core.controls import Button
from flappy_animal.core.utils import Even_value
class BasicScene:
    def __init__(self, name, window) -> None:
        self.name = name
        self.window = window
        self.font = None
        self.background = None
        self.text_boxes = []
        self.button_boxes = []

    def add_background(self, background_image):
        self.window.set_background(image=background_image)
        # self.window.blit(self.background, (0, 0))

    def add_textbox(self, text, antialiasing, color, location, font, size):
        self.font = PyGameWrapper.set_font(font, size)
        text_surf = self.font.render(text, antialiasing, color)
        # self.window.blit(text_surf, location)
        self.text_boxes.append((text_surf, location))

    def add_button(self, name, location, image, func=None):
        button = (Button(name, location, image, self.window, func))
        self.button_boxes.append(button)

    def update(self, window):
        for box in self.text_boxes:
            self.window.blit(box[0], box[1])
        for button in self.button_boxes:
            button.draw()